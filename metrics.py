def compute_metrics(jobs, completion_times):
    turnaround = {}
    waiting = {}
    
    for job in jobs:
        pid = job["pid"]
        arrival = job["arrival"]
        burst = job["burst"]
        end = completion_times[pid]

        turnaround[pid] = end - arrival
        waiting[pid] = turnaround[pid] - burst

    avg_turnaround = sum(turnaround.values()) / len(jobs)
    avg_waiting = sum(waiting.values()) / len(jobs)

    return {
        "turnaround": turnaround,
        "waiting": waiting,
        "avg_turnaround": round(avg_turnaround, 2),
        "avg_waiting": round(avg_waiting, 2)
    }
