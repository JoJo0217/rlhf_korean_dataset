import json
import random

# Load data from train.json
result =[]
#with open("rm2_final.jsonl", "r", encoding="utf-8") as file:
#    for line in file:
#        result.append(json.loads(line))

with open("./step3/hatespeech_sol/merged.jsonl", "r", encoding="utf-8") as file:
        result=json.load(file)

data=result
# Randomly extract 100 items
random.seed(42)  # To ensure reproducibility, set the random seed
random_indices = random.sample(range(len(data)), 400)
extracted_data = [data[i] for i in random_indices]

# Create two separate lists: extracted_data (100 items) and remaining_data (the rest)
remaining_data = [item for i, item in enumerate(data) if i not in random_indices]

# Save the extracted 100 items to a new JSON file
with open("gpt_eval.json", "w", encoding="utf-8") as file:
    json.dump(extracted_data, file, ensure_ascii=False, indent=4)

# Save the remaining data to another JSON file
with open("gpt_train.json", "w", encoding="utf-8") as file:
    json.dump(remaining_data, file, ensure_ascii=False, indent=4)
