#!/usr/bin/env python

import cv2
import time
import datetime

print('写真撮影開始')


deviceid=0  #  もし内臓カメラではなくてUSBカメラなどを使う場合は1にしてください
capture = cv2.VideoCapture(deviceid,cv2.CAP_DSHOW)


#  写真を「現在時刻.jpg」という名前で保存
dt_now = datetime.datetime.now()
dt_str_now = dt_now.strftime('%m%d%H%M%S')
ret, frame = capture.read()
time.sleep(1)
cv2.imwrite(dt_str_now + '.jpg', frame)

print(dt_str_now + '.jpgという名前で画像が保存されました！''')