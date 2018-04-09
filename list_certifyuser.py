#coding=utf-8

import time,sys
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#将一个列表的元素弹出后移动到另一个列表
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    time.sleep(1.5)
    print("Verifying user: " + current_user.title()) 
    confirmed_users.append(current_user)
