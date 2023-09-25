step1을 위한 데이터셋 입니다.

데이터의 품질을 위해 koalpaca v1.0 5만개 데이터와 oig 1만개의 데이터를 직접 gpt3.5 16k turbo를 통해 자연스럽게 전처리하는 과정을 진행하였습니다.
prompt는 다음과 같습니다.   
<pre>
<code>
아래의 JSON 객체를 한국어로 번역해주세요. 
번역 시 단, {"instruction": "", "input": "", "output": “”}구조를 유지하고, 존댓말, 대화체 사용 및 가독성을 고려해주세요:
</code>
</pre>   
이후 추가로 깨진 데이터, 번역 안된 데이터는 추가로 수동 검수했습니다.   

2023-9-25   
오픈 어시스턴트 data에서 오픈 어시스턴트를 포함하는 데이터 삭제   
-> 답변에 오픈 어시스턴트라고 하는 경우가 나오기 때문   
또한 스탠포드 대학 번역 데이터에서 번역 과정에서 input에 입력 이라는 부분이 추가된 부분 삭제

***
데이터 링크   
instruction, input, output의 구조  
https://huggingface.co/datasets/jojo0217/korean_rlhf_dataset
   
***
데이터 구성   
|데이터 종류|개수|url|
|:---|---:|---:|
|koalpaca v1.1|21155|https://github.com/Beomi/KoAlpaca|
|stanford alpaca|51374|https://huggingface.co/datasets/tatsu-lab/alpaca|
|dolly|15009|https://huggingface.co/datasets/nlpai-lab/databricks-dolly-15k-ko|
|openassistant|9651|https://huggingface.co/datasets/nlpai-lab/openassistant-guanaco-ko|
|oig_chip2|10000|https://huggingface.co/datasets/0-hero/OIG-small-chip2|
|총합|107189||