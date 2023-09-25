import json
import jsonlines
load_file="../step1/train/train.jsonl"
save_file="../step1/train/train.jsonl"
# eval.json 파일 로드
with open(load_file, "r", encoding="utf-8") as file:
    #data = json.load(file)
    data = [json.loads(line) for line in file.readlines()]

# "### 질문: "과 "### 답변: "을 prompt에 붙이기
filtered_word='<unk>'
result=[]
for item in data:
    #item["prompt"] = f"### 질문: {item['prompt']} ### 답변: "
    #if 'output' not in item:
    #    continue
    if filtered_word in item['output'] or filtered_word in item['input'] or filtered_word in item['instruction'] :
        continue
    else:
        result.append(item)
# 수정된 데이터를 새로운 JSON 파일로 저장
with jsonlines.open(save_file, mode='w') as writer:
    for one_data in result:
        writer.write(one_data)
