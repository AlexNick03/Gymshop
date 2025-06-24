import json

models_to_keep = {
    "products.product",
    
}

with open('dump.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filtered_data = [entry for entry in data if entry['model'] in models_to_keep]

with open('products_only.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, indent=2, ensure_ascii=False)

print(f"Filtered {len(filtered_data)} entries to products_only.json")