import sys
from scheduler import schedule
from io_utils import read_input, write_output

def main():
    input_file = sys.argv[1]

    data = read_input(input_file)

    policy = data["policy"]
    jobs = data["jobs"]
    quantum = data.get("quantum")

    result = schedule(policy, jobs, quantum)

    write_output(result)

if __name__ == "__main__":
    main()
