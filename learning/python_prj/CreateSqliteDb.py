#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
' a test module '

__author__ = 'Michael Liao'

import sqlite3
import sys
import m_age
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

name = input('name:')
agein = input('age:') 
age = int(agein)
res = m_age.greeting(name,age) 
print(res)

configDb = sqlite3.connect("/home/config.db") 
configDb.execute("create table apn (apnid integer primary key,profileid integer not null, apnname varchar(10) not null UNIQUE, nickname text NULL)")
for t in[(0,10,'epc.com','Yu'),(1,20,'cmnet','Xu')]:
  configDb.execute("insert into apn values (?,?,?,?)", t)
configDb.commit()
configDb.execute("select apnname from apn")
#configDb.fetchall()
configDb.close()
