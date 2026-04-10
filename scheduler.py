from fifo import fifo

def schedule(policy, jobs, quantum=None):
    if policy == "FIFO":
        return fifo(jobs)