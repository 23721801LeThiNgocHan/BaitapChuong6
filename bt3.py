# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:28:55 2024

@author: PC
"""

a=input("Nhập số nguyên dương: ")
N=int(a)
S=(N//10)+(N%10)
if 10<=N<=99:
   print("Chữ số thứ nhất: ",N//10)
   print("Chữ số thứ hai: ",N%10)
   print("Tổng 2 số là: ",S)

