from pathlib import Path

from cairo_rs_py import CairoRunner

contracts_path = Path("compiled-contracts")

if not contracts_path.exists():
    raise Exception(f"required directory {contracts_path} doesn't exist, please, compile cairo programs")

for path in contracts_path.glob("*.json"):
    print(f"running {path}")
    with open(path) as file:
        runner = CairoRunner(file.read(), "main", "all", False)
        result = runner.cairo_run(False)

print("DONE")
