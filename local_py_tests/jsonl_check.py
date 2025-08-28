import json
from pathlib import Path

jsonl_dir = Path("/home/dave_sava/AdaParse/output_json/parsed_pdfs")  # change to your output folder
required_fields = ["title", "authors", "text"]  # adjust if your schema differs

for file in jsonl_dir.glob("*.jsonl"):
    print(f"\nChecking {file.name}")
    with file.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                print(f"  Line {i}: INVALID JSON")
                continue

            missing = [field for field in required_fields if field not in entry]
            empty_text = not entry.get("text", "").strip()

            if missing or empty_text:
                print(f"  Line {i}: Missing fields {missing}, empty text: {empty_text}")
