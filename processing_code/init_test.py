import json

with open('/home/dave_sava/AdaParse/output_json/parsed_pdfs/5af6168a-ec63-41d0-8eba-a81e4c156ab8.jsonl', 'r') as f:
    data = [json.loads(line) for line in f]

print(data[0])  # first parsed PDF
