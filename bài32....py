# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:28:52 2024

@author: HP
"""

a=float(input("so km xe taxi da di duoc: "))
if a<=1 :
    st=a*15000
if 1<a<=5:
    st=(a-1)*13500+15000
if a>5:
    st=15000+4*13500+(a-5)*11000
if a>120:
    st=0.9*(15000+4*13500+(a-5)*11000)
print("tien cuoc taxi: ",st)