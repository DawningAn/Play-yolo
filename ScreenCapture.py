# python捕获屏幕
import numpy as np
import cv2
import time
from PIL import ImageGrab

count = 0

while 1:
    count = count + 1
    img = ImageGrab.grab(bbox=(430,160,1750,920))  # xmin,ymin,xmax,ymax
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    cv2.imshow('s',frame)

    if count == 50:
        t = time.time() * 1000
        count = 0

    cv2.waitKey(10)

