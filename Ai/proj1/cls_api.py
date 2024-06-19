# fast API 확인 용도

# from typing import Union  
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

from fastapi import FastAPI, File, UploadFile

# STEP 1: Import the necessary modules. # 모델을 잘 쓰기위한 모듈을 설치하거나 임포트 작업
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision


# STEP 2: Create an ImageClassifier object. #중요해 !! 추론기를 만든다 미디어파이프에는 기본적인 모델을 가져오고 모델경로 지정 
# STEP 1 과 STEP 2 는 FastAPI 실행 전에 만들어서 서버가 뜨고 루프가 돌때 함께 한번만 실행 하도록한다
# FastAPI 만든 후에 추론기를 만들면 통신 실행마다 모델이 들어오게 되어 지연 상태가 된다.
base_options = python.BaseOptions(model_asset_path='models\\efficientnet_lite0.tflite') # 베이스 옵션에 모델 옵션을 넣어준다.
options = vision.ImageClassifierOptions(base_options=base_options, max_results=3) # task에 모델옵션을 넣어주고 모델 아웃풋이 max_results 는 몇개를 할것인가 설정
classifier = vision.ImageClassifier.create_from_options(options)

app = FastAPI()


# @app.post("/files/")
# async def create_file(file: bytes = File()):
#     return {"file_size": len(file)}

import io
import PIL
import numpy as np

# upload 로 할 경우는 read 를 해줘야 실제 파일이 넘어옴 
# 그 이전에는 메타 데이터만 넘어가 있음
# jpg 가 아닌 png 등 다른 확장자 파일들을 사용할때 타입 예외 처리 가능
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    
    byte_file = await file.read() # 바이트파일로 들어온 데이터를 변환시켜줘야함

    # # STEP 3: Load the input image. # 추론할 대상 데이터를 가져온다 이미지 로드 
    # image = mp.Image.create_from_file(IMAGE_FILENAMES[1])

    # convert char array to binary array
    image_bin = io.BytesIO(byte_file) # 기계어로 읽을 수 없는 텍스트 형태이기 때문에 읽을수 있는 이미지 바이너리로 바꿔주고

    # create PIL Image from binary array 
    pil_img = PIL.Image.open(image_bin) # 이미지 바이너리를 

    # convert MP Image from PIL IMAGE
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.asarray(pil_img))

    # STEP 4: Classify the input image. # 추론
    classification_result = classifier.classify(image)
    print(classification_result)

    # STEP 5: Process the classification result. In this case, visualize it. # 추론 후처리 단계 어떻게 보여줄건지 고민
    # top_category = classification_result.classifications[0].categories[o]
    # # result = (f"{top_category.category_name} ({top_category.score:.2f})")
    count = 3
    results = []
    for i in range(count):
        category = classification_result.classifications[0].categories[i]
        results.append({"category":category.category_name,"score": category.score})

    return {"result":results}

    # return {"result": {
    #     "category": top_category.category_name,
    #     "score": top_category.score
    # }}

    #print(result)

    #return {"filename": file.filename}
    #return {"filename": len(byte_file)}