list1=[]
list2=[]
n=int(input("enter the size of color in list1:"))
m=int(input("enter the size of color in list2:"))
print("enter elements of l1:")
for i in range(0,n):
    list1.append((input()))
print("enter elements of l2:")
for i in range(0,m):
    list2.append((input()))
print(list(set(list1)-set(list2)))
