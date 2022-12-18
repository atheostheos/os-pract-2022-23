#!/usr/bin/env python
import os
import random
import time

import fire


def run_process(s: int) -> None:
    pid = os.getpid()
    ppid = os.getppid()

    print(f"Сhild[{pid}]: I am started. My PID {pid}. Parent PID {ppid}.")
    time.sleep(s)
    print(f"Child[{pid}]: I am ended. PID {pid}. Parent PID {ppid}.")

    exit_status = random.randint(0, 1)
    os._exit(exit_status)


if __name__ == "__main__":
    fire.Fire(run_process)


