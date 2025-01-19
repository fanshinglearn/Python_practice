# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 22:36:31 2022

@author: USER
"""

x2=x3=x4=x5=x6=x7=x8=x9=x10=x11=x12=0
for i in range(1,7):
    for j in range(1,7):
        #print("%d%d"%(i,j),"\t",end="")
        if i+j==2:
            x2+=1
        elif i+j==3:
            x3+=1
        elif i+j==4:
            x4+=1
        elif i+j==5:
            x5+=1
        elif i+j==6:
            x6+=1
        elif i+j==7:
            x7+=1
        elif i+j==8:
            x8+=1
        elif i+j==9:
            x9+=1
        elif i+j==10:
            x10+=1
        elif i+j==11:
            x11+=1
        elif i+j==12:
            x12+=1
    #print()
print()

print("2點出現的機率=",x2,"/36")
print("3點出現的機率=",x3,"/36")
print("4點出現的機率=",x4,"/36")
print("5點出現的機率=",x5,"/36")
print("6點出現的機率=",x6,"/36")
print("7點出現的機率=",x7,"/36")
print("8點出現的機率=",x8,"/36")
print("9點出現的機率=",x9,"/36")
print("10點出現的機率=",x10,"/36")
print("11點出現的機率=",x11,"/36")
print("12點出現的機率=",x12,"/36")