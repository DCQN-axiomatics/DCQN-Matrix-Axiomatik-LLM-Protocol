import json
import sys

def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

prompt = load("example_prompt.txt")
output = load("example_llm_output.txt")

required_flags = [
    "STATUS_STEP1 = JA_DOI_ZUGRIFF",
    "STATUS_STEP2 = JA_VOLLTEXT_GELESEN"
]

missing = [f for f in required_flags if f not in output]

if missing:
    print("DETERMINISM CHECK: FAIL")
    print("Missing:", missing)
    sys.exit(1)

print("DETERMINISM CHECK: PASS")
print("All required flags present.")
