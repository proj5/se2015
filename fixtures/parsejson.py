import json

filename = "users.json"

with open(filename, 'r') as handle:
    new_json = json.load(handle)

f = open(filename, 'w')
f.write(json.dumps(new_json, indent=2, sort_keys=True))
