# -*-coding:utf-8-*-

# def fortune(f0, p, c0, n, i):
# 	for x in range(1,n):
# 		f0=int(f0*(1+p/100)-c0)
# 		c0=int(c0*(1+i/100)	)
# 	return f0>0

#print(fortune(100000,1,9185,12,1))

# Test.describe("fortune")
# Test.it("Basic tests")
# Test.assert_equals(fortune(100000, 1, 2000, 15, 1), True)
# Test.assert_equals(fortune(100000, 1, 9185, 12, 1), False)
# Test.assert_equals(fortune(100000000, 1, 100000, 50, 1), True)
# Test.assert_equals(fortune(100000000, 1.5, 10000000, 50, 1), False)
# Test.assert_equals(fortune(100000000, 5, 1000000, 50, 1), True)
# ####################################################################

def revrot(strng, sz):
    numlist=[]
    newlist=[]
    for x in strng:
    	numlist.append(x)
    if sz<= 0 or sz > len(strng) or strng=="":
    	return ""
    if int(strng) % 2 == 0:
    	newlist=numlist[1:sz]

    return newlist

#test
t=revrot("123456",4)
print(t)
n="123456"
L=[]
for x in n:
	L.append(x)
print(L[2])
