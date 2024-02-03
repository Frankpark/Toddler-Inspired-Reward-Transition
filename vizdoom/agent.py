import torch
import torch.nn.functional as F
from torch.autograd import Variable
from torch.nn.utils import clip_grad_norm_

import numpy as np
from utils import ensure_shared_grads

from params import params

def preprocess(obs, gpu_id):
    state = torch.from_numpy(np.array(obs, dtype='f')) / 255.   #
    width, height = state.size()[2], state.size()[3]
    state = state.view(-1, width, height).unsqueeze(0)
    with torch.cuda.device(gpu_id):
        state = state.cuda()

    return state

def postprocess(logit):
    prob = F.softmax(logit, dim=-1)
    log_prob = F.log_softmax(logit, dim=-1)
    entropy = -(log_prob * prob).sum(1)
    action = prob.multinomial(1).data
    log_prob = log_prob.gather(1, Variable(action))
    action = action.cpu().numpy()
    return action, entropy, log_prob

class A3CAgent(object):
    def __init__(self, model, gpu_id):
        self.model = model
        self.hx, self.cx = None, None
        self.eps_len = 0
        self.values = []
        self.log_probs = []
        self.rewards = []
        self.entropies = []
        self.done = False
        self.gpu_id = gpu_id
        self.n_update = 0

    def action_train(self, obs, target_idx):
        state = preprocess(obs, self.gpu_id)

        value, logit, self.hx, self.cx = self.model(state, target_idx, self.hx, self.cx)
        action, entropy, log_prob = postprocess(logit)

        self.eps_len += 1
        return np.squeeze(action, axis=0), entropy, value, log_prob, logit

    def action_test(self, obs, target_idx):
        state = preprocess(obs, self.gpu_id)

        with torch.no_grad():
            value, logit, self.hx, self.cx = self.model(state, target_idx, self.hx, self.cx)
        prob = F.softmax(logit, dim=1)
        action = prob.max(1)[1].data.cpu().numpy()

        self.eps_len += 1
        return action, value, logit, prob


    def synchronize(self, shared_model):
        with torch.cuda.device(self.gpu_id):
            self.model.load_state_dict(shared_model.state_dict())
            self.cx = Variable(torch.zeros(1, 256).cuda())
            self.hx = Variable(torch.zeros(1, 256).cuda())

    def put_reward(self, reward, entropy, value, log_prob):
        self.rewards.append(reward)
        self.entropies.append(entropy)
        self.values.append(value)
        self.log_probs.append(log_prob)

    def clear_actions(self):
        self.values.clear()
        self.log_probs.clear()
        self.rewards.clear()
        self.entropies.clear()

    def training(self, next_obs, target_idx, shared_model, shared_optimizer, entropy_coef):
        self.model.train()

        self.n_update += 1
        self.cx = Variable(self.cx.data)
        self.hx = Variable(self.hx.data)

        R = torch.zeros(1, 1)
        if not self.done:
            state = preprocess(next_obs, self.gpu_id)
            value, logit, _, _ = self.model(state, target_idx, self.hx, self.cx)

            R = value.data

        if self.gpu_id >= 0:
            with torch.cuda.device(self.gpu_id):
                R = R.cuda()
        R = Variable(R)
        self.values.append(R)

        policy_loss = 0
        value_loss = 0
        gae = torch.zeros(1, 1)

        if self.gpu_id >= 0:
            with torch.cuda.device(self.gpu_id):
                gae = gae.cuda()

        for i in reversed(range(len(self.rewards))):
            R = params.gamma * R + self.rewards[i]
            advantage = R - self.values[i]
            value_loss = value_loss + 0.5 * advantage.pow(2)

            # Generalized Advantage Estimation
            delta_t = params.gamma * self.values[i + 1].data - self.values[i].data + self.rewards[i]

            gae = gae * params.gamma * params.tau + delta_t

            policy_loss = policy_loss - self.log_probs[i] * Variable(gae) - entropy_coef * self.entropies[i]

        shared_optimizer.zero_grad()
        loss = policy_loss + params.value_loss_coef * value_loss
        loss.backward()
        clip_grad_norm_(self.model.parameters(), params.clip_grad_norm)
        ensure_shared_grads(self.model, shared_model, gpu=self.gpu_id >= 0)

        shared_optimizer.step()
        with torch.cuda.device(self.gpu_id):
            self.model.load_state_dict(shared_model.state_dict())

        self.clear_actions()