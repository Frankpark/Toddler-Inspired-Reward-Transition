import torch
import torch.nn as nn
import torch.nn.functional as F


class A3C_LSTM_GA(torch.nn.Module):
    def __init__(self):
        super(A3C_LSTM_GA, self).__init__()
        ## convolution network
        self.conv1 = nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1)
        self.batchnorm1 = nn.BatchNorm2d(32, track_running_stats=False)
        self.conv2 = nn.Conv2d(32, 32, kernel_size=3, stride=2, padding=1)
        self.batchnorm2 = nn.BatchNorm2d(32, track_running_stats=False)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1)
        self.batchnorm3 = nn.BatchNorm2d(64, track_running_stats=False)
        self.conv4 = nn.Conv2d(64, 64, kernel_size=3, stride=2, padding=1)
        self.batchnorm4 = nn.BatchNorm2d(64, track_running_stats=False)

        self.fc = nn.Linear(64*3*3, 256)

        # Instruction Processing, MLP
        self.embedding = nn.Embedding(5, 25)
        self.target_att_linear = nn.Linear(25, 256)

        ## a3c-lstm network
        self.lstm = nn.LSTMCell(512, 256)

        self.mlp = nn.Linear(512, 256)

        self.mlp_policy = nn.Linear(256, 64)
        self.policy = nn.Linear(64, 3)

        self.mlp_value = nn.Linear(256, 32)  # 64
        self.value = nn.Linear(32, 1)

    def forward(self, state, target_idx, hx, cx):
        x = state

        x = F.relu(self.batchnorm1(self.conv1(x)))
        x = F.relu(self.batchnorm2(self.conv2(x)))
        x = F.relu(self.batchnorm3(self.conv3(x)))
        x = F.relu(self.batchnorm4(self.conv4(x)))

        x = x.view(x.size(0), -1)
        img_feat = F.relu(self.fc(x))

        word_embedding = self.embedding(target_idx)
        word_embedding = word_embedding.view(word_embedding.size(0), -1)

        word_embedding = self.target_att_linear(word_embedding)
        gated_att = torch.sigmoid(word_embedding)

        gated_fusion = torch.mul(img_feat, gated_att)
        lstm_input = torch.cat([gated_fusion, word_embedding], 1)

        _hx, _cx = self.lstm(lstm_input, (hx, cx))


        mlp_input = torch.cat([gated_fusion, _hx], 1)
        mlp_output = F.relu(self.mlp(mlp_input))

        policy = F.relu(self.mlp_policy(mlp_output))

        value = F.relu(self.mlp_value(mlp_output))

        return self.value(value), self.policy(policy), _hx, _cx
