from fifo import fifo
from sjf import sjf
from rr import rr
from priority import priority_schedule

def schedule(policy, jobs, quantum=None):
    policy = policy.upper()

    if policy == "FIFO":
        return fifo(jobs)
    elif policy == "SJF":
        return sjf(jobs)
    elif policy == "RR":
        return rr(jobs, quantum)
    elif policy == "PRIORITY":
        return priority_schedule(jobs)
    else:
        raise ValueError(f"Unsupported policy: {policy}")
