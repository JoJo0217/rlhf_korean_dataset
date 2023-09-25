import json
import jsonlines

data=[]
file_name='./step1/train/train.jsonl'
save_name=file_name
del_name='id'
with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        data.append( json.loads(line))

for one in data:
    keys=list(one.keys())
    for key in keys:
        if key != 'instruction' and key !='input' and key !='output':
            del one[key]
    if 'input' not in one:
        one['input']=''

with jsonlines.open(save_name, mode='w') as writer:
    for one_data in data:
        writer.write(one_data)

