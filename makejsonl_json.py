import json

data=[]
file_name='./step3/hatespeech_sol/merged.jsonl'
save_name=file_name.replace("jsonl","json")

with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        data.append( json.loads(line))

with open(save_name, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)