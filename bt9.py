# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:19:55 2024

@author: PC
"""

import math
a=float(input("a= "))
b=float(input("b= "))
a1= math.sqrt(a) - math.sqrt(b)
a2= a**(1/4) - b**(1/4)
a3= math.sqrt(a) + (a*b)**(1/4)
a4= a**(1/4) + b**(1/4)
T=(a1/a2) - (a3/a4)
print("Kết quả là: ",T)