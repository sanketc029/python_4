from functools import *

no=int(input("Enter the number"))
lst=list()
for i in range(no):
    lst.append(int(input()))
print("The given lis is ==",lst)

even=list(filter(lambda lst:not(lst%2),lst))
print("Even no",even)
sqrs=list(map(lambda lst:lst*lst,even))
print("square of no",sqrs)
total=reduce(lambda lst1,lst2:lst1+lst2,sqrs)
print("The total of all no",total)


'''def printeven(lst):
    if lst%2==0:
        return lst
def sqr(lst):
    return lst*lst
def sum(lst1,lst2):
    return lst1+lst2
    
no=int(input("Enter the number"))
lst=list()
for i in range(no):
    lst.append(int(input()))
print("The given lis is ==",lst)

even=list(filter(printeven,lst))
print("Even no",even)
sqrs=list(map(sqr,even))
print("square of no",sqrs)
total=reduce(sum,sqrs)
print("The total of all no",total)    '''