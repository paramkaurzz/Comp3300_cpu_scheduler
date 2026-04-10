import json
from fifo import fifo

with open("sample_input.json", "r") as f:
    data = json.load(f)

result = fifo(data["jobs"])

print(json.dumps(result, indent=2))