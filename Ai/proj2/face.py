# STEP 1
import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

# STEP 2
# app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider']) 나중에 GPU 를 쓸때 CUDA를 쓰면됨.
# app = FaceAnalysis(providers=['CPUExecutionProvider'])

app = FaceAnalysis(providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

# STEP 3
# img = ins_get_image('t1')
img = cv2.imread('k1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('k2.jpg', cv2.IMREAD_COLOR)

# STEP 4
faces1 = app.get(img)
faces2 = app.get(img2)

# STEP 5
# rimg = app.draw_on(img, faces)
# cv2.imwrite("./t1_output.jpg", rimg)

print(len(faces1))
print(len(faces2))
# print(faces[0].embedding)

# GIT 에서 examples/demo_analysis.py 에서 복사해옴 
# # then print all-to-all face similarity 
# feats = []
# for face in faces:
#     feats.append(face.normed_embedding)
# feats = np.array(feats, dtype=np.float32)
# sims = np.dot(feats, feats.T)
# print(sims)

# then print all-to-all face similarity
# feats = []
# feats.append(faces[0].normed_debedding)
# feats.append(faces[0].normed_debedding)

# feats = np.array(feats, dtype=np.float32) # 넘파일 데이터로 바꿔서 사용해야한다.
# sims = np.dot(feats[0], feats[1].T) # 유사도 계산시 DOT 계산 
# print(sims)


# feats = []
# feats.append(faces[0].normed_debedding)
# feats.append(faces[0].normed_debedding)

feats1 = np.array(faces1[0].normed_embedding, dtype=np.float32) # 넘파일 데이터로 바꿔서 사용해야한다.
feats2 = np.array(faces2[0].normed_embedding, dtype=np.float32)

sims = np.dot(feats1, feats2.T) # 유사도 계산시 DOT 계산 
print(sims)