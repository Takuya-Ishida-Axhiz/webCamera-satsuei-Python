#!/usr/bin/env python

import cv2
import time
import datetime
import schedule
import boto3


# 【作業1】　先ほど控えたアクセスキーとシークレットアクセスキーと差し替えてください
#  流出注意
accesskey = "IAMのアクセスキー"
secretkey = "IAMのシークレットアクセスキー"

region = "ap-northeast-1"

s3 = boto3.client('s3', aws_access_key_id=accesskey, aws_secret_access_key= secretkey, region_name=region)



print('写真撮影開始')

deviceid=0 #もし内臓カメラではなくてUSBカメラなどを使う場合は1にしてください
capture = cv2.VideoCapture(deviceid,cv2.CAP_DSHOW)


def job():
    dt_now = datetime.datetime.now()
    dt_str_now = dt_now.strftime('%m%d%H%M%S')
    ret, frame = capture.read()
    time.sleep(1)
    cv2.imwrite(dt_str_now + '.jpg', frame)
    print(dt_str_now + '.jpgという名前で画像がPCに保存されました！''')
    
    # 【作業2】アップロード先のバケット名を、ご自身で作成されたバケット名に差し替えてください。例："ishida-python-face-picture"
    filename = dt_str_now + '.jpg'
    bucket_name = "アップロード先のバケット名"

    s3.upload_file(filename,bucket_name,filename)
    print("{0}　がS3にアップロードされました！".format(filename))



#  10秒に一度写真を撮るように設定しています。
schedule.every(1/6).minutes.do(job)

#  注意！Ctrl+Cで黒い画面を消さないとずっと写真を撮り続けます！
while True:
  schedule.run_pending()
  time.sleep(1)