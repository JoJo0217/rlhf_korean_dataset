step2를 위한 dataset입니다.  

step2 chosen, rejected를 만들기 위해
koalpaca의 답변을 2개 만들고 인간이 직접 ranking을 만든 데이터도 있지만   
실험 과정에서 그 데이터는 답변이 비슷하여 reward model 학습 후 테스트 과정에서 어느것이 chosen이고 어느것이 rejected인지 구별을 못하는 문제가 생겼습니다.   
그렇기에 지금 데이터는 명확한 답변을 주기 위해 SFT로 1단계 처리한 모델을 rejected에 넣고 ChatGPT3.5의 답변을 chosen에 넣은 데이터입니다.   

hatespeech 부분은 따로 SFT 단계에서 학습시킨 모델의 답변이 G-eval 과정에서 ChatGPT를 이기는 결과를 보였고    
실제로 ChatGPT는 hatespeech 부분에서 답변을 잘 못하는 것이 보였기에   
hatespeech 데이터만 chosen에 SFT모델을 넣었고 rejected에 ChatGPT 답변을 넣었습니다.

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
