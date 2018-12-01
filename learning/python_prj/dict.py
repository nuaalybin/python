#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = input('input your name:')

name = str(n)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
#error
#if d[name]:	
if name in d:	
    print('hello %s score is %d'%(name,d[name]))
else:
    print('no score')
print('len',len(d))