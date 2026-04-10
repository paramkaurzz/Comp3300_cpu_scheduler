def fifo(jobs):
    # sort by arrival time, then PID (tie-break rule)
    jobs = sorted(jobs, key=lambda x: (x["arrival"], x["pid"]))

    time = 0
    gantt = []
    turnaround = {}
    waiting = {}

    for job in jobs:
        pid = job["pid"]
        arrival = job["arrival"]
        burst = job["burst"]

        if time < arrival:
            time = arrival

        start = time
        end = time + burst
        time = end

        gantt.append({
            "pid": pid,
            "start": start,
            "end": end
        })

        turnaround[pid] = end - arrival
        waiting[pid] = turnaround[pid] - burst

    avg_turnaround = sum(turnaround.values()) / len(jobs)
    avg_waiting = sum(waiting.values()) / len(jobs)

    return {
        "policy": "FIFO",
        "gantt": gantt,
        "metrics": {
            "turnaround": turnaround,
            "waiting": waiting,
            "avg_turnaround": round(avg_turnaround, 2),
            "avg_waiting": round(avg_waiting, 2)
        }
    }