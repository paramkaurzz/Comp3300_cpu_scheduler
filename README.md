# :floppy_disk: CPU Scheduling Simulator (COMP3300)
This project implements a simulation of classical CPU scheduling algorithms including First-In-First-Out (FIFO), Shortest Job First (SJF), Round Robin, and Priority scheduling. It computes scheduling timelines and performance metrics and produces a JSON output. 

This project was created for COMP3300 Operating Systems Fundamentals in collaboration with Paramjit Sidhu, Alissa Mac Neil, Jasman Saran, and Emmanuel Musinguzi. 

## :bar_chart: Algorithms
**In the event of tiebreaks**, the lexicographically smallest PID is used for all algorithms.
1. **FIFO (First In, First Out)**: Processes are executed in the order they arrive in. 
2. **SJF (Shortest Job First)**: Waiting processes with the smallest execution (burst) time are executed first. This implementation is non-preemptive.
3. **Round Robin**: Each process is assigned a fixed time slice and waiting processes run in a circular fashion.
4. **Priority**: Each process is assigned a priority value and those with the lowest numerical value (highest importance) are executed first. This implementation is non-preemptive.

## :arrow_forward: Usage
### Requirements
1. Python 3
2. Input provided as JSON
3. Output printed as JSON

Run the program using:
```
python3 main.py input.json > output.json
```


### Input Format
Input is taken as a JSON file specifying policy, quantum, and jobs. Each job must include:
- **Process ID (PID)**: The unique identifier for the process.
- **Arrival Time**: When the process arrives to the CPU. 
- **Burst Time**: Total amount of time the process requires to execute.
- **Priority**: If applicable, the numerical priority value; lower values are prioritized.
The Quantum field is only required for Round Robin scheduling and not present in others. 

A sample input for Round Robin is preloaded into `input.json`. Other samples can be found in the `sample_inputs` folder, one for each scheduling algorithm.

```
{
  "policy": "",
  "quantum": 0,
  "jobs": [
    {"pid": "A", "arrival": 0, "burst": 6, "priority": 3},
    {"pid": "B", "arrival": 0, "burst": 2, "priority": 1},
    {"pid": "C", "arrival": 1, "burst": 3, "priority": 2}
  ]
}
```

### Output Format
Output is received in JSON output and includes:
- **Gantt Chart**: Timeline of process execution (start and end times).
- **Waiting Time**: Amount of time the process spent ready and waiting in the queue.
- **Turnaround Time**: Time elapsed from a task's arrival to completed execution. 

```
{
    "policy": "" ,
    "gantt": [
        {"pid": "A" , "start": 0 , "end": 2},
        {"pid": "B" , "start": 2 , "end": 4}
    ],
    "metrics": {
        "turnaround": {"A": 10 , "B": 4 , "C": 7} ,
        "waiting": {"A": 4 , "B": 2 , "C": 4} ,
        "avg_turnaround": 7.00 ,
        "avg_waiting": 3.33
    }
}
```

## :file_folder: Project Structure
```
Comp3300_cpu_scheduler/
├── main.py                  # Entry point of the program
├── scheduler.py             # Dispatches scheduling algorithms based on policy
├── fifo.py                  # First-In-First-Out (FIFO) scheduling implementation
├── sjf.py                   # Shortest Job First (SJF) scheduling implementation
├── rr.py                    # Round Robin scheduling implementation
├── priority.py              # Priority scheduling implementation
├── metrics.py               # Turnaround, waiting time, and averages calculation
├── io_utils.py              # JSON input parsing and output formatting utilities
│
├── sample_inputs/             # Sample scheduling data used in testing
│   ├── fifo_input.json
│   ├── sjf_input.json
│   ├── rr_input.json
│   └── priority_input.json
│
├── sample_outputs/            # Sample outputs produced by data in sample_inputs
│   ├── fifo_output.json
│   ├── sjf_output.json
│   ├── rr_output.json
│   └── priority_output.json
│
├── input.json              # Generic test input
├── output.json             # Generic output file
├── README.md
```

## :red_circle: AI Usage Disclaimer
:construction: This section is under construction and awaiting addition from the rest of the project team.
- This project's README was human-written but AI was used for refinement and clarity of the final structure.
-
-