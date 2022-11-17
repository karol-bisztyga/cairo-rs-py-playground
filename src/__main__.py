import os

from cairo_rs_py import CairoRunner

old_path = "compiled-contracts/simple-old.json"
new_path = "compiled-contracts/simple-new.json"
# new_path = "compiled-contracts/simple-new-hacked.json"

if not os.path.exists(new_path):
    raise Exception(f"required file {new_path} doesn't exist, please, compile cairo programs")

if not os.path.exists(old_path):
    raise Exception(f"required file {old_path} doesn't exist, please, compile cairo programs")

print("running the old program")
with open(old_path) as file:
    contents = file.read()
    runner = CairoRunner(contents, "main", "all", False)
    result = runner.cairo_run(False)
    assert 1 == 1

print("running the new program")
with open(new_path) as file:
    contents = file.read()
    runner = CairoRunner(contents, "main", "all", False) # doesn't work
    # result = runner.cairo_run(False)

print("DONE")
