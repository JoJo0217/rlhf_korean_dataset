step2를 위한 dataset입니다.  

|데이터 종류|개수|url|
|:---|---:|---:|
|감성 대화|720|https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=86|
|yitingxie|3927|https://huggingface.co/datasets/yitingxie/rlhf-reward-datasets|
|혐오 표현|490|https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=558|
|일상 대화|409|https://corpus.korean.go.kr/request/reausetMain.do?lang=ko|
|총합|5546||


step2는 답변으로 chosen은 gpt3.5 turbo 16k의 답변으로 생성을 하였고
rejected는 kullm-v2 base model에서 2500개의 추가 일상대화 데이터로 sft 학습을 진행한 모델로 답변을 넣었습니다.

step2 raw datasets.jsonl은 yitingxie에서 수동으로 검수한 3900개의 데이터에 chosen에 gpt3.5의 답변을 넣었고 rejected에 ourmodel의 답변을 넣었습니다.
