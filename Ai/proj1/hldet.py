import cv2
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np

MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54) # vibrant green

def draw_landmarks_on_image(rgb_image, detection_result):
  hand_landmarks_list = detection_result.hand_landmarks
  handedness_list = detection_result.handedness
  annotated_image = np.copy(rgb_image)

  # Loop through the detected hands to visualize.
  for idx in range(len(hand_landmarks_list)):
    hand_landmarks = hand_landmarks_list[idx]
    handedness = handedness_list[idx]

    # Draw the hand landmarks.
    hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    hand_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      hand_landmarks_proto,
      solutions.hands.HAND_CONNECTIONS,
      solutions.drawing_styles.get_default_hand_landmarks_style(),
      solutions.drawing_styles.get_default_hand_connections_style())

    # Get the top left corner of the detected hand's bounding box.
    height, width, _ = annotated_image.shape
    x_coordinates = [landmark.x for landmark in hand_landmarks]
    y_coordinates = [landmark.y for landmark in hand_landmarks]
    text_x = int(min(x_coordinates) * width)
    text_y = int(min(y_coordinates) * height) - MARGIN

    # Draw handedness (left or right hand) on the image.
    cv2.putText(annotated_image, f"{handedness[0].category_name}",
                (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

  return annotated_image


IMAGE_FILE = 'womanhands.jpg'
MODEL_PATH = 'models/hand_landmarker.task'

# import cv2

# img = cv2.imread(IMAGE_FILE)
# #cv2_imshow(img)
# cv2.imshow("test", img)
# cv2.waitKey(0)

# STEP 1: Import the necessary modules.
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# STEP 2: Create an HandLandmarker object.
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

# # STEP 3: Load the input image.
# image = mp.Image.create_from_file(IMAGE_FILE)

# # STEP 4: Detect hand landmarks from the input image.
# detection_result = detector.detect(image)
# print(detection_result)

# # STEP 5: Process the classification result. In this case, visualize it.
# annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)
# # cv2_imshow(cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
# cv2.imshow("test", annotated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Real-time video stream processing function
def process_frame(image, detector, timestamp):
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
    detector.detect_async(mp_image, timestamp)

# STEP 6: Using webcam for real-time hand detection
cap = cv2.VideoCapture(0)  # Using the webcam
if not cap.isOpened():
    print("Cannot open webcam.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # frame_timestamp_ms = int(cap.get(cv2.CAP_PROP_POS_MSEC))
    # process_frame(frame, detector, frame_timestamp_ms)

    detection_result = detector.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=frame))
    annotated_image = draw_landmarks_on_image(frame, detection_result)
    cv2.imshow('Hand Detection Live', annotated_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
