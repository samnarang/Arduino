# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:36:55 2019

@author: samna
"""
String n;
n = input("sadljkf");
int i=0,cnt = 0;
while(i<n.length()) :
    if(n.charAt(i)==' ') :
        cnt = cnt+1;
    i = i+1;
print(cnt);        