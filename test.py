# -*- coding: utf-8 -*-

import re
from collections import OrderedDict
from collections import Counter

s='cdafcbdcdbd'
sc=Counter()
for x in s:
	sc[x]=sc[x]+1

print(sc)