import json

input_file_path = "compiled-contracts/simple-new.json"
output_file_path = "compiled-contracts/simple-new-hacked.json"

hacked = None

with open(input_file_path, 'r') as file:
  hacked = json.loads(file.read())
  for k, v in hacked["program"].items():
    if hacked.get(k):
      raise Exception(f"key {k} already present in the json root")
    hacked[k] = v
  del hacked["program"]



with open(output_file_path, 'w') as file:
  file.write(json.dumps(hacked, sort_keys=True, indent=4, separators=(',', ': ')))

print("DONE")