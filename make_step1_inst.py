import json
import jsonlines
# 원본 JSON 파일을 읽습니다.
with open("./step1/train.json", "r") as in_file:
    data = json.load(in_file)

# 프로세스 및 변환을 위한 데이터를 저장할 리스트를 생성합니다.
processed_data = []

# 입력된 데이터를 분석합니다.
for item in data:
    original_prompt = item["prompt"]

    # 중요한 부분을 추출하려고 매칭
    instruction_sign = "### 질문: "
    context_sign = "### 맥락: "
    output_sign = "### 답변: "

    instruction = original_prompt.partition(instruction_sign)[2].partition("###")[0].strip()
    context = original_prompt.partition(context_sign)[2].partition("###")[0].strip() if context_sign in original_prompt else ""
    output = original_prompt.partition(output_sign)[2].strip()

    processed_data.append({
        "instruction": instruction,
        "input": context,
        "output": output
    })

# jsonl 파일로 변환된 데이터를 저장합니다.
#with open("processed_data.jsonl", "w") as out_file:
#    for item in processed_data:
#        out_file.write(json.dumps(item) + '\n')
with jsonlines.open("filtered.jsonl", mode='w') as writer:
    for one_data in processed_data:
        writer.write(one_data)