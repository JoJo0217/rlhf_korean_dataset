from sentence_transformers import SentenceTransformer, util
import json
import numpy as np
import jsonlines

embedder = SentenceTransformer("jhgan/ko-sroberta-multitask")

# Load jsonl data into a Python list of dictionaries
data = []
with open("./step2/mk6/raw_data/gamseong.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        data.append(json.loads(line))

# Get the prompts from the data
# Set a similarity threshold and initialize an empty set for duplicates
similarity_threshold = 0.9 # Adjust this value according to your needs
duplicates = set()
duplicates_list = []
sub_list=[]
num_same=0
for i in range(len(data)):
    prompt_embedding=embedder.encode(data[i]['prompt'],convert_to_tensor=True)
    chosen_embedding=embedder.encode(data[i]['chosen'],convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(prompt_embedding, chosen_embedding)[0]
    cos_scores = cos_scores.cpu().numpy()
    if(cos_scores>similarity_threshold):
        duplicates_list.append(i)
        num_same+=1
        print("유사도: ",cos_scores)
        print("index: ",i)
        print("prompt: ",data[i]['prompt'])
        print("chosen: ",data[i]['chosen'])
print("같은 것들의 숫자: ",num_same)

with jsonlines.open("filtered.jsonl", mode='w') as writer:
    for idx,one_data in enumerate(data):
        if idx not in duplicates_list:
            writer.write(one_data)
with jsonlines.open("similar.jsonl", mode='w') as writer:
    for idx,one_data in enumerate(data):
        if idx in duplicates_list:
            writer.write(one_data)