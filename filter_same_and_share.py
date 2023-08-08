import json
import jsonlines

# 첫 번째 jsonl 파일을 읽습니다.
with open("./step2/no_hate.jsonl", "r") as file1:
    data1 = [json.loads(line) for line in file1.readlines()]

# 두 번째 jsonl 파일을 읽습니다.
with open("./whole_gamseong.jsonl", "r") as file2:
    data2 = [json.loads(line) for line in file2.readlines()]

# 두 번째 파일에 있는 prompts를 추출합니다.
prompts_in_file2 = {item["prompt"] for item in data2}

# 첫 번째 파일에서 두 번째 파일에 없는 prompt를 가진 데이터만 필터링합니다.
filtered_data = [item for item in data1 if item["prompt"] not in prompts_in_file2]

# 첫 번째 파일에서 두 번째 파일에 있는 prompt를 가진 데이터만 필터링합니다.
shared_data = [item for item in data1 if item["prompt"] in prompts_in_file2]

# 첫 번째 파일의 데이터 중 두 번째 파일에 없는 데이터만 저장합니다.

with jsonlines.open("filtered_data.jsonl", mode='w') as writer:
    for one_data in filtered_data:
        writer.write(one_data)

with jsonlines.open("shared_data.jsonl", mode='w') as writer:
    for one_data in shared_data:
        writer.write(one_data)
