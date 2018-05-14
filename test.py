# -*- coding: utf-8 -*-

import re

# st0= '0a,1b,2c,1d 2E 3F 4g 3h 4'

# print('split:',st0.split('1'))
# print('re.split:',re.split('[a-h]',st0))
# print('re.split:',re.split('[a-h]',st0,0,flags=re.IGNORECASE))
# print('re.split:',re.split('[,\s]',st0))
# print('re.split:',re.split('([,\s])',st0))
# print('re.findall:',re.findall(r'\w{2}',st0))
# print('re.findall:',re.findall(r'(\w{2})',st0))

re_telephone = re.compile(r'^(\d{3})-(\d{3})@(\d{1,3})$')
s=re_telephone.match('010-123@45').groups()
print(s)