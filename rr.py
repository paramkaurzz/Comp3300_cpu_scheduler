from collections import deque
from metrics import compute_metrics

def rr(jobs, quantum):
    if quantum is None or quantum <= 0:
        raise ValueError("Round Robin requires a positive quantum")

    # sort jobs by arrival time, then PID for tie-breaking
    jobs = sorted(jobs, key=lambda x: (x["arrival"], x["pid"]))

    time = 0
    gantt = []
    completion = {}
    ready = deque()

    # keep track of remaining burst time per process
    remaining = {job["pid"]: job["burst"] for job in jobs}

    i = 0
    n = len(jobs)

    while i < n or ready:
        # add all jobs that have arrived by current time
        while i < n and jobs[i]["arrival"] <= time:
            ready.append(jobs[i])
            i += 1

        # if no ready jobs, jump to next arrival
        if not ready:
            time = jobs[i]["arrival"]
            while i < n and jobs[i]["arrival"] <= time:
                ready.append(jobs[i])
                i += 1

        current_job = ready.popleft()
        pid = current_job["pid"]

        start = time
        run_time = min(quantum, remaining[pid])
        end = time + run_time

        gantt.append({
            "pid": pid,
            "start": start,
            "end": end
        })

        time = end
        remaining[pid] -= run_time

        # add any jobs that arrived during this time slice
        while i < n and jobs[i]["arrival"] <= time:
            ready.append(jobs[i])
            i += 1

        # if not finished, requeue at the back
        if remaining[pid] > 0:
            ready.append(current_job)
        else:
            completion[pid] = time

    metrics = compute_metrics(jobs, completion)

    return {
        "policy": "RR",
        "gantt": gantt,
        "metrics": metrics
    }
