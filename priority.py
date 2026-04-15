from metrics import compute_metrics

def priority_schedule(jobs):
    time = 0
    gantt = []
    completion = {}
    completed_jobs = set()

    length = len(jobs)

    while len(completed_jobs) < length:
        # jobs that have arrived and are not done
        to_do_jobs = [
            job for job in jobs
            if job["arrival"] <= time and job["pid"] not in completed_jobs
        ]

        if not to_do_jobs:
            # jump to next arrival if CPU is idle
            time = min(
                job["arrival"] for job in jobs
                if job["pid"] not in completed_jobs
            )
            continue

        # smaller priority number = higher priority
        # tie-break by PID
        current_job = min(to_do_jobs, key=lambda x: (x["priority"], x["pid"]))

        start = time
        end = time + current_job["burst"]

        gantt.append({
            "pid": current_job["pid"],
            "start": start,
            "end": end
        })

        time = end
        completion[current_job["pid"]] = end
        completed_jobs.add(current_job["pid"])

    metrics = compute_metrics(jobs, completion)

    return {
        "policy": "PRIORITY",
        "gantt": gantt,
        "metrics": metrics
    }
