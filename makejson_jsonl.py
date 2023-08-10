import json
import jsonlines

data=[]
file_name='./step3/hatespeech_sol/merged.jsonl'
save_name=file_name+'l'
with open(file_name, "r", encoding="utf-8") as file:
        data=json.load(file)

with jsonlines.open(save_name, mode='w') as writer:
    for one_data in data:
        writer.write(one_data)