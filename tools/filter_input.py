import json
import jsonlines
load_file="./step1/rawdata/step1_stanford.jsonl"
save_file="./step1/rawdata/step1_stanford.jsonl"
# eval.json 파일 로드
with open(load_file, "r", encoding="utf-8") as file:
    #data = json.load(file)
    data = [json.loads(line) for line in file.readlines()]

# "### 질문: "과 "### 답변: "을 prompt에 붙이기
for item in data:
    #item["prompt"] = f"### 질문: {item['prompt']} ### 답변: "
    if 'input' not in item:
        item['input']=""
    if '입력 없음' in item['input'] or '입력없음' in item['input'] or 'noinput' in item['input'].lower() or 'no input' in item['input'].lower() :
        item['input']=""
# 수정된 데이터를 새로운 JSON 파일로 저장
with jsonlines.open(save_file, mode='w') as writer:
    for one_data in data:
        writer.write(one_data)
