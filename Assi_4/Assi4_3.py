#Using lambda functions
from functools import *

def findless(lst):
    for i in range(lst):
        if (lst >= 70 and lst <=90)  :
            return lst

no=int(input("Enter the no"))
lst=[]
for num in range(no):
    lst.append(int(input()))
sortedele=list(filter(findless,lst))
print("Sorted data ",sortedele)
modified=list(map(lambda lst:lst + 10,sortedele))
print("after addition ",modified)
result=reduce(lambda lst1,lst2:lst1*lst2,modified)
print("After the reduce multiplication",result)




'''
with nornam named function
def findless(lst):
    for i in range(lst):
        lst=int(lst)
        if (lst >= 70 and lst <=90)  :
            return lst

def increase(lst):
    return lst+10

def mul(lst1,lst2):
    return lst1+lst2

no=int(input("Enter the no"))
t=[]
for num in range(no):
    ele=int(input())
    t.append(input())

arr=list(filter(findless,t))
brr=list(map(increase,arr))
crr=reduce(mul,brr)
print("After the reduce multiplication",crr)'''

