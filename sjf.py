from metrics import compute_metrics

def sjf(jobs):
    time = 0
    gantt = []
    completion = {}
    completed_jobs = set()

    length = len(jobs)

    while len(completed_jobs) < length:
        #find the jobs that need to be completed
        to_do_jobs = [job for job in jobs
            if job["arrival"] <= time and job["pid"] not in completed_jobs]

        if not to_do_jobs:
            #move to next job
            time = min(job["arrival"] for job in jobs
                       if job["pid"] not in completed_jobs)
            continue

        # choose shortest job
        current_job = min(to_do_jobs, key=lambda x: (x["burst"], x["pid"]))
        start = time
        end = time + current_job["burst"]

        #add to gantt chart
        gantt.append({"pid": current_job["pid"], "start": start, "end": end})

        time = end
        completion[current_job["pid"]] = end
        completed_jobs.add(current_job["pid"])

    metrics = compute_metrics(jobs, completion)

    return {
        "policy": "SJF",
        "gantt": gantt,
        "metrics": metrics
    }
