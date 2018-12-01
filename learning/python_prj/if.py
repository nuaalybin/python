#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = input('input your name:')


if name == 'lucy':
    print('Hello ',name)
else:
    print('not lucy, Hello',name)


s = input('input your age:')

age = int(s)

if age>18:
    print('older')
else:
	print('yaunger')