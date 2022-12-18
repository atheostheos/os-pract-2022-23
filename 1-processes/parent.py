import os
import random
import fire

PARENT_PID = 0
CHILD_PROGRAM = "child.py"


def fork_process() -> int:
    """
    Forks a new process and returns child pid in parent process
    :return: child pid
    """
    child_pid = os.fork()

    if child_pid != PARENT_PID:
        print(f"Parent[{PARENT_PID}]: I ran children process with PID {child_pid}.")
    else:
        randint = str(random.randint(5, 10))
        os.execv(CHILD_PROGRAM, ["-s", randint])

    return child_pid


def run_processes(amount: int) -> None:
    # start child processes
    children_list = {fork_process() for i in range(amount)}

    while children_list:
        child_pid, status = os.wait()
        # convert status to exit code
        status = os.WEXITSTATUS(status)
        if child_pid != PARENT_PID:
            print(f"Parent[{PARENT_PID}]: Child with PID child_pid terminated. Exit Status {status}.")
            children_list.remove(child_pid)
            if status != 0:
                children_list.add(fork_process())


if __name__ == "__main__":
    # Use automatic CLI generator
    # E.g. python parent.py --amount=4
    fire.Fire(run_processes)
