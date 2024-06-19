IMAGE_FILENAMES = ['burger.jpg', 'cat.jpg']

import cv2
import math

DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480

# def resize_and_show(image):
#   h, w = image.shape[:2]
#   if h < w:
#     img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
#   else:
#     img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
# #   cv2_imshow(img)
#   cv2.imshow("test",img)
#   cv2.waitKey(0)


# # Preview the images.

# images = {name: cv2.imread(name) for name in IMAGE_FILENAMES}
# for name, image in images.items():
#   print(name)
#   resize_and_show(image)




# STEP 1: Import the necessary modules. # 모델을 잘 쓰기위한 모듈을 설치하거나 임포트 작업
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision

# STEP 2: Create an ImageClassifier object. #중요해 !! 추론기를 만든다 미디어파이프에는 기본적인 모델을 가져오고 모델경로 지정 
base_options = python.BaseOptions(model_asset_path='models\\efficientnet_lite0.tflite') # 베이스 옵션에 모델 옵션을 넣어준다.
options = vision.ImageClassifierOptions(base_options=base_options, max_results=1) # task에 모델옵션을 넣어주고 모델 아웃풋이 max_results 는 몇개를 할것인가 설정
classifier = vision.ImageClassifier.create_from_options(options)


# STEP 3: Load the input image. # 추론할 대상 데이터를 가져온다 이미지 로드 
image = mp.Image.create_from_file(IMAGE_FILENAMES[0])

# STEP 4: Classify the input image. # 추론
classification_result = classifier.classify(image)

# STEP 5: Process the classification result. In this case, visualize it. # 추론 후처리 단계 어떻게 보여줄건지 고민
top_category = classification_result.classifications[0].categories[0]
result = (f"{top_category.category_name} ({top_category.score:.2f})")

print(result)

# display_batch_of_images(images, predictions)