import os
import cv2
import numpy as np
from PIL import Image
import json
import io
DATA_PATH=r"C:\Users\Lincoln1080Ti\PycharmProjects\repos\Keras-FCN-master\result\AtrousFCN_Resnet50_16s320square5"
# DATA_PATH=r"Test"
RES_PATH=os.path.join(DATA_PATH,"refineseg")
IMG_FMT=".png"
resfiles = [f for f in os.listdir(RES_PATH) if os.path.isfile(os.path.join(RES_PATH, f)) and f.endswith(IMG_FMT)]
first=True
for file in resfiles:
    dbname, rest = file.split('_')
    imgnum, _ = rest.split('.')
    id=0
    if dbname == "CVC-300":
        id = 1 * 10000 + int(imgnum)
    elif dbname == "CVC-612":
        id = 2 * 10000 + int(imgnum)
    img_path = os.path.join(RES_PATH, file)

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    height,width = img.shape
    ret, thresh = cv2.threshold(img, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, 2)
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        if not first:
            a=np.concatenate((a,np.array([[id,x,y,w,h,1,1]])), axis=0)
        else:
            a=np.array([[id,x,y,w,h,1,1]])
            first=False
    np.save('result.npy',a)
print a.shape
