import json

def read_input(filename):
    with open(filename, "r") as f:
        return json.load(f)

def write_output(data):
    print(json.dumps(data, indent=2))