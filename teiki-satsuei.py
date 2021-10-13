#!/usr/bin/env python

import cv2
import time
import datetime
import schedule

print('写真撮影開始')

deviceid=0 #  もし内臓カメラではなくてUSBカメラなどを使う場合は1にしてください
capture = cv2.VideoCapture(deviceid,cv2.CAP_DSHOW)


def job():
    dt_now = datetime.datetime.now()
    dt_str_now = dt_now.strftime('%m%d%H%M%S')
    ret, frame = capture.read()
    time.sleep(1)
    cv2.imwrite(dt_str_now + '.jpg', frame)
    print(dt_str_now + '.jpgという名前で画像が保存されました！''')



#  10秒に一度写真を撮るように設定しています。
schedule.every(1/6).minutes.do(job)

#  注意！Ctrl+Cで黒い画面を消さないとずっと写真を撮り続けます！
while True:
  schedule.run_pending()
  time.sleep(1)
