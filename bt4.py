# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:52:24 2024

@author: PC
"""

time=input("Nhập giờ,phút,giây(nhập dưới dạng':'): ")
hh, mm, ss = map(int, time.split(":"))
if 0<= hh <24 and 0<=mm<60 and 0<=ss<60:
    T= hh*3600 + mm*60 + ss
    print("Đổi được là: ",T)
else:
    print("Không định dạng được")