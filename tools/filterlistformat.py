import json
import jsonlines
data=[]
with open("./step2/remove_similar/step2_yitingxie_raw.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        data.append(json.loads(line))
        

listformat=[]    
for idx,onedata in enumerate(data):
    if '1.' in onedata['chosen']:
        listformat.append(idx)

with jsonlines.open("filtered.jsonl", mode='w') as writer:
    for idx,one_data in enumerate(data):
        if idx not in listformat:
            writer.write(one_data)
with jsonlines.open("similar.jsonl", mode='w') as writer:
    for idx,one_data in enumerate(data):
        if idx in listformat:
            writer.write(one_data)