from metrics import compute_metrics

def fifo(jobs):
    # sort by arrival time, then PID (tie-break rule)
    jobs = sorted(jobs, key=lambda x: (x["arrival"], x["pid"]))

    time = 0
    gantt = []
    completion = {}

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

        completion[pid] = end

    metrics = compute_metrics(jobs, completion)

    return {
        "policy": "FIFO",
        "gantt": gantt,
        "metrics": metrics
    }