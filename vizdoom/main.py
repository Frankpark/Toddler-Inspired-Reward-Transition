import os
os.environ["OMP_NUM_THREADS"] = "1"
import torch.multiprocessing as mp

import time

from train import run_sim
from eval import test
from shared_optim import SharedAdam
from models import A3C_LSTM_GA
from params import params, log_params


def main():
    log_params()

    mp.set_start_method('spawn')
    count = mp.Value('i', 0)
    lock = mp.Lock()

    shared_model = A3C_LSTM_GA()
    shared_model = shared_model.share_memory()

    shared_optimizer = SharedAdam(shared_model.parameters(), lr=params.lr, amsgrad=params.amsgrad,
                                  weight_decay=params.weight_decay)
    shared_optimizer.share_memory()

    # run_sim(0, shared_model, shared_optimizer, count, lock) # DEBUG
    # test(0, shared_model, shared_optimizer, count, lock) #DEBUG

    processes = []

    for rank in range(params.num_train_processes):
        p = mp.Process(target=run_sim, args=(rank, shared_model, shared_optimizer, count, lock, params))
        p.start()
        processes.append(p)

    start_time = time.time()

    for rank in range(params.num_test_processes):
        p = mp.Process(target=test, args=(
            rank, shared_model, shared_optimizer, count, lock, params, start_time
        ))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


if __name__ == "__main__":
    main()
