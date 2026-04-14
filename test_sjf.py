import json
from sjf import sjf

with open("sample_input.json", "r") as f:
    data = json.load(f)

result = sjf(data["jobs"])

print(json.dumps(result, indent=2))
