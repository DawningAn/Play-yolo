'''
根据训练好的模型，进行推理
'''
import cv2
import numpy as np
import torch
import time

class detector:
    def __init__(self):
        # 加载模型
        self.model = torch.hub.load('./yolov5-master','custom',path = './best_weights/ppe_yolo_n.pt',source='local')
        self.model.conf = 0.4
        # 获取视频流
        self.cap = cv2.VideoCapture(0)


    def detect(self):
        while True:

            ret,frame = self.cap.read()

            frame = cv2.flip(frame,1)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            result = self.model(frame)
            result_pd = result.pandas().xyxy[0].to_numpy()

            print(result_pd)
            # 绘制边界框
            for box in result_pd:
                l,t,r,b = box[:4].astype('int')
                label_id = box[5]
                if label_id == 0:
                    cv2.rectangle(frame,(l,t),(r,b),(0,255,0),4)
                else:
                    cv2.rectangle(frame,(l,t),(r,b),(255,0,0),4)



            print(result_pd)

            cv2.imshow('demo_detector',frame)
            if cv2.waitKey(10) & 0xFF == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()


myDetect = detector()
myDetect.detect()