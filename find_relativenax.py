#-*- utf-8 -*-

import random
#构造一个函数,找出偏离平均值最大的数
def find_peak(list):
	ave=sum(list)/len(list)
	maxdelta=0
	for x in list:
		delta=abs(x-ave)		
		if delta > maxdelta:
			peak = x
			maxdelta=delta
	return peak

mynum=[random.randint(1,500) for i in range(100)]
test=[5,8,7,5,9,3,2,25,5]
posi=mynum.index(find_peak(mynum))+1
print('List:',mynum)
print('最大值:%d;最小值:%d;平均值:%f'%(max(mynum),min(mynum),sum(mynum)/len(mynum)))
print('偏差最大的值是:%d;位于第%d位。'%(find_peak(mynum),posi))