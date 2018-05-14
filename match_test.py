# -*- coding: utf-8 -*-

import re

# # version 1
# def is_valid_email(addr):
#     check_mail=re.compile(r'\w+\.?\w+@\w+\.com$')
#     if check_mail.match(addr):
#     	return True   


# # 测试:
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert is_valid_email('mr.bob@example.com')
# print('ok')

# verion 2
def name_of_email(addr):
    m = re.match(r'^\<?([a-zA-Z\s]*)>?.*@(.+)$', addr)
    return m.group(1)

# print(name_of_email('<Tom Paris> tom@voyager.org'))
# print(name_of_email('tom@voyager.org'))
# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')