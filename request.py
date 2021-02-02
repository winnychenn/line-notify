#!/usr/bin/env python3
# coding=utf8

import datetime 
import requests
from table import table

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
 
    
# 修改為你要傳送的訊息內容
message = '亞爾大笨蛋'
# 修改為你的權杖內容
token = 'N2t8a0XQS43ps1MpWEdIfBU3qyUlza1w5JZ9krk7lMb'
token2 = 'eD0kajWXCsWf7FOWgfbxGJB8b93nZAEp1VMD5VFHv9I'

#lineNotifyMessage(token, message)

if __name__ == '__main__':
    x=datetime.datetime.now() + datetime.timedelta(hours = +8)
    y=datetime.datetime.now() + datetime.timedelta(hours = -2)
    z=y + datetime.timedelta(hours = +1)
    #print(y)
    #print(z)
    #print("{}點".format(y.hour))
    #print("{}點".format(z.hour))
    #print("星期{}".format(y.weekday()+1))
    #print("星期{}".format(z.weekday()+1))
    #message='\n星期{} {}點 \n'.format(x.weekday()+1,x.hour)+table(y.hour,y.weekday())
    #nextmessage='\n下個時段\n星期{} {}點 \n'.format(x.weekday()+1,x.hour+1)+table(z.hour,z.weekday())
    message='\n'+table(y.hour,y.weekday())
    nextmessage='\n下個時段 '+table(z.hour,z.weekday())
    #print(message)
    #print(nextmessage)
    lineNotifyMessage(token, message+nextmessage)
    print(y.weekday())
    if y.weekday() == 0 and y.hour == 0:
        lineNotifyMessage(token2, "今天記得買vip點數")
        lineNotifyMessage(token, "今天記得買vip點數")
    if y.weekday() == 2 and y.hour == 0:
        lineNotifyMessage(token2, "今天記得買vip戰爭徽章")
        lineNotifyMessage(token, "今天記得買vip戰爭徽章")
    if y.weekday() == 3 and y.hour == 0:
        lineNotifyMessage(token2, "今天記得買vip金卡")
        lineNotifyMessage(token, "今天記得買vip金卡")
    #lineNotifyMessage(token, nextmessage)

