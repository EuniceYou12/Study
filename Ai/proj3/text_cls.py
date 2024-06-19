# STEP 1. import modules
from transformers import pipeline
# from transformers import AutoTokenizer,AutoModelForSequenceClassification

# # STEP 2.
# tokenizer = AutoTokenizer.from_pretrained("stevhliu/my_awesome_model")
# model = AutoModelForSequenceClassification.from_pretrained("stevhliu/my_awesome_model")


# STEP 2. create inference instance 추론기 만들기
# Huggingface 에서 pipeline 에 모든것이 들어가 있다 첫번째로 task name 두번째로 모델이 들어간다.
# model 앞에 이름이 없으면 내 계정에서 모델을 찾게되고 로그인이 안되어 있을경우 에러 발생
# classifier = pipeline("sentiment-analysis", model="stevhliu/my_awesome_model")
classifier = pipeline("sentiment-analysis", model="snunlp/KR-FinBert-SC")

# STEP 3. prepare input data
# text = "This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might be my favorite of the three."
text = "삼성전자 주가가 허락했다"

# STEP 4. inference
result = classifier(text)

# # STEP 4.
# inputs = tokenizer(text, return_tensors="pt")
# with torch.no_grad():
#     logits = model(**inputs).logits

# 4-1. preprocessing(data -> tensor(blob)) 사람이 읽을수 있는 data 가 모델이 읽어줄수 있는 data가 되고
# 4-2. inference(tensor(blob) -> logit) 
# 4-3. postprocessing(logit -> data)

# STEP 5. visualize
print(result)