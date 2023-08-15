import json
import jsonlines

with open("koalpaca_rlhf6.jsonl", "r",encoding="utf-8") as file1:
    data1 = [json.loads(line) for line in file1.readlines()]
    
for i in range(len(data1)):
    del data1[i]['id']
    data1[i]["chosen"]=""
    data1[i]["rejected"]=""

with jsonlines.open("removed.jsonl", mode='w') as writer:
    for one_data in data1:
        writer.write(one_data)