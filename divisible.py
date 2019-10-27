# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:46:41 2019

@author: samna
"""
i=1000
cnt=0
while(i<2000):
  if i%7==0:
    if i%5!=0:
        cnt=cnt+1
        print("no ",i,"cnt",cnt) 
  i=i+1