import json

# 1. eval.json 파일 로드
with open("train3.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 2. "### 질문: "과 "### 답변: " 부분 제거
for item in data:
    item["prompt"] = item["prompt"].replace("### 질문: ", "").replace("### 답변: ", "").strip()

# 3. 수정된 데이터를 새로운 JSON 파일로 저장
with open("train_f.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)