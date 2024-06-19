from fastapi import FastAPI, File, UploadFile

# STEP 1: Import the necessary modules.
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# STEP 2: Create an ObjectDetector object.
base_options = python.BaseOptions(model_asset_path='models/efficientdet_lite0.tflite')
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.5)
detector = vision.ObjectDetector.create_from_options(options)

app = FastAPI()


# @app.post("/files/")
# async def create_file(file: bytes = File()):
#     return {"file_size": len(file)}

import cv2
import io
import PIL

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):

    byte_file = await file.read() # 바이트파일로 들어온 데이터를 변환시켜줘야함

    # # STEP 3: Load the input image.
    # image = mp.Image.create_from_file(IMAGE_FILE)

    # convert char array to binary array
    image_bin = io.BytesIO(byte_file) # 기계어로 읽을 수 없는 텍스트 형태이기 때문에 읽을수 있는 이미지 바이너리로 바꿔주고

    # create PIL Image from binary array 
    pil_img = PIL.Image.open(image_bin) # 이미지 바이너리를 

    # convert MP Image from PIL IMAGE
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.asarray(pil_img))

    # STEP 4: Detect objects in the input image.
    detection_result = detector.detect(image)
    print(detection_result)

    # STEP 5: Process the detection result. In this case, visualize it.
    # image_copy = np.copy(image.numpy_view()) 
    # annotated_image = visualize(image_copy, detection_result)
    # rgb_annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    # # cv2_imshow(rgb_annotated_image)
    # cv2.imshow("test", rgb_annotated_image)
    # cv2.waitKey(0)

    #return {"filename": file.filename}



    # results = []
    # for detection in detection_result.detections:
    #     category = detection.categories[0]
    #     results.append({"category": category.category_name, "score": category.score})

    # return {"filename": file.filename, "detections_count": len(detection_result.detections), "detections": results}



    # category_counts = {}
    # for detection in detection_result.detections:
    #     category = detection.categories[0].category_name
    #     if category in category_counts:
    #         category_counts[category] += 1
    #     else:
    #         category_counts[category] = 1

    # return {"filename": file.filename, "category_counts": category_counts}



    # category_counts = {}
    # for detection in detection_result.detections:
    #     category = detection.categories[0].category_name
    #     if category in category_counts:
    #         category_counts[category] += 1
    #     else:
    #         category_counts[category] = 1

    # formatted_results = [{"category": category, "count": count} for category, count in category_counts.items()]

    # return formatted_results


    # DetectionResult(
    # detections=[
    #   Detection(
    #       bounding_box=BoundingBox(origin_x=72, origin_y=162, width=252, height=191), 
    #       categories=[Category(index=None, score=0.7798683643341064, display_name=None, category_name='cat')], 
    #       keypoints=[]), 
    #   Detection(
    #       bounding_box=BoundingBox(origin_x=303, origin_y=27, width=248, height=344), 
    #       categories=[Category(index=None, score=0.7624295949935913, display_name=None, category_name='dog')], 
    #       keypoints=[])])

    det_result = []
    for detection in detection_result.detections:
        print(detection.categories[0].category_name)
        det_result.append(detection.categories[0].category_name)

    return {"result": det_result}