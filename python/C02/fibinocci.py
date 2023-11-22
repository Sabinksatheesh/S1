def fibnocci(n):
    if n<0:
        return 0
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibnocci(n-2)+fibnocci(n-1)
count=int(input("enter Num:"))
for i in range(0,count):
    print(fibnocci(i))