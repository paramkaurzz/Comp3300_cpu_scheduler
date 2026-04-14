from fifo import fifo
from sjf import sjf

def schedule(policy, jobs, quantum=None):
    if policy == "FIFO":
        return fifo(jobs)
    elif policy == "SJF":
        return sjf(jobs)
