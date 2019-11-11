
from functools import *

def isprime(data):
    for num in range(data):
        if data > 1:
            for i in range(2, data):
                if (data % i) == 0:
                    break
            else:
                return(data)

def multby2(data):
    return data*2

def ismax(data1,data2):
    if data1 < data2:
        return data2
    else:
        return data1

num=int(input("Enter the no"))
data=list()

for i in range(num):
    data.append(int(input()))
print("List data",data)
primedata=list(filter(isprime,data))
print("Filtered prime data",primedata)
multdata=list(map(multby2,primedata))
print("Multiplied by 2 to all prime no",multdata)
finaldata=reduce(ismax,multdata)
print("Highest no from data",finaldata)