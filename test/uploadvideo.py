# -*- coding: utf-8 -*-
# 测试上传视频2个， 运行格式: `python uploadvideo.py 2` 
import swiftclient
import os
import sys
import datetime

# swift info
user = 'swiftuser1:swiftsubuser1'
key = '8Us5blLxYeh77cqWQR9qhgWT3e8BMOu8zokeKB3k'
rootdir = "./upload/"
count = sys.argv[1]
# container name
container_name = 'swiftuser1-container1'

# connect swift
conn = swiftclient.Connection(
        user=user,
        key=key,
        authurl='http://192.168.0.134:8080/auth',
)

# uploadfile
def uploadFile(pathName,num):
    if not num.isdigit():
        print('please input number')
        return
    num = int(num)
    print('start uploading')
    start = datetime.datetime.now()
    # read all file
    f = open(rootdir + '/video.txt', 'r')
    file_names = f.readlines()
    # Guarantee not to cross the borde
    temp = len(file_names) if num > len(file_names) else num
    if temp != num:
        print('The test may be unreasonable Insufficient number of documents')
    num = temp
    for i in range(num):
        filepath = pathName + '/' + file_names[i].strip('\n')
        conn.put_object(container_name, file_names[i].strip('\n'), open(filepath, 'rb'))
    end = datetime.datetime.now()
    print('test upload location ' + pathName +  ' number: ' + num.__str__() + ' spend time:' + (end-start).total_seconds().__str__() + 'microseconds')

#  upload file 500
uploadFile(rootdir,num=count)

