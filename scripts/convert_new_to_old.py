import json

def convert(contract):
  print(f"converting {contract}...")
  input_file_path = f"compiled-contracts/{contract}.json"
  output_file_path = f"compiled-contracts/{contract}-hacked.json"
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

new_contracts = ["simple-new", "account"]

for contract in new_contracts:
  convert(contract)

print("DONE")
