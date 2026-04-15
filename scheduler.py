from fifo import fifo
from sjf import sjf
from rr import rr

def schedule(policy, jobs, quantum=None):
    if policy == "FIFO":
        return fifo(jobs)
    elif policy == "SJF":
        return sjf(jobs)
    elif policy == "RR":
        return rr(jobs, quantum)
    else:
        raise ValueError(f"Unsupported policy: {policy}")
