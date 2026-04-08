def compute_metrics(jobs, completion_times):
    turnaround = {}
    waiting = {}
    total_ta = 0
    total_wt = 0

    for job in jobs:
        pid = job["pid"]
        ta = completion_times[pid] - job["arrival"]
        wt = ta - job["burst"]
        turnaround[pid] = ta
        waiting[pid] = wt
        total_ta += ta
        total_wt += wt

    n = len(jobs)
    return {
        "turnaround": turnaround,
        "waiting": waiting,
        "avg_turnaround": round(total_ta / n, 2) if n else 0,
        "avg_waiting": round(total_wt / n, 2) if n else 0
    }
