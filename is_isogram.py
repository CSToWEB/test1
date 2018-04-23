# -*- coding:utf-8 -*-

'''
introduction：
An isogram is a word that has no repeating letters, consecutive or 
non-consecutive. Implement a function that determines whether a string that
contains only letters is an isogram. Assume the empty string is an isogram. 
Ignore letter case.
'''

#codewars community best practices solution
def is_isogram(string):
    return len(string) == len(set(string.lower()))

def my_isogram(string):
    s_lowcase=string.lower()
    n=len(s_lowcase)
    if n==0:
        return True
    else:
        for i in s_lowcase:
            sum=0
            for j in range(n):
                if i==s_lowcase[j]:
                    sum+=1
            if sum>1:
                return False
                break
        return True

s1='a2b c'
s2='EOF5864abfc'
s3=''
print(is_isogram(s1),is_isogram(s2),is_isogram(s3))
print(my_isogram(s1),my_isogram(s2),my_isogram(s3))