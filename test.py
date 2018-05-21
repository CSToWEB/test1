# -*- coding: utf-8 -*-

s1 = "LOL"
s2 = "HOW R U"	#, 13
s3 = 'WHERE DO U WANT 2 MEET L8R'

#构建一个字典，查询输入每个字母的按键次数
STRING_TO_INT = {
	'2': 4,
	'8': 4,
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 1,
    'E': 2,
    'F': 3,
    'G': 1,
    'H': 2,
    'I': 3,
    'J': 1,
    'K': 2,
    'L': 3,
    'M': 1,
    'N': 2,
    'O': 3,
    'P': 1,
    'Q': 2,
    'R': 3,
    'S': 4,
    'T': 1,
    'U': 2,
    'V': 3,
    'W': 1,
    'X': 2,
    'Y': 3,
    'Z': 4,
    ' ': 1
}

def str_2_int(ch):
	return STRING_TO_INT[ch]

def presses(phrase):
	T = 0
	s_upp = phrase.upper()
	myset = set(s_upp)
	for x in myset:
		T = T + s_upp.count(x)*str_2_int(x)
	return T

#testcase
print(presses(s3))