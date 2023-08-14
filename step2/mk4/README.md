mk4 데이터 입니다.   

bert 모델로 prompt와 chosen의 similar 정도가 0.9보다 큰 것들을 걸러내서   
거의 동일한 답변이 들어가는 것을 방지했습니다.   

yitingxie dataset의 개수를 list형식 답변을 기존 1500개에서 500개로 줄이고   
list형식 아닌 답변은 2407개에서 1500개만 넣어서 yitingxie 데이터의 개수를 2000개로 줄였습니다.