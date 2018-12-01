#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#input
name = input()
print('Hello,', name)
#list
classmates = ['Michael', 'Bob', 'Tracy']

print('list num',len(classmates))

print('classmates[1]',classmates[1])
print('classmates',classmates)
classmates.insert(1, 'Jack')

print('classmates[1]',classmates[1])
print('classmates',classmates)

classmates.append('Adam')
print('classmates',classmates)

classmates.pop()
print('classmates',classmates)

classmates.pop(1)
print('classmates',classmates)



#tuple

classmates = ('Michael', 'Bob', 'Tracy')

print('tuple num',len(classmates))

print('classmates[1]',classmates[1])
print('classmates',classmates)