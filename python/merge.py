dict1 = {}
l1 = int(input("Enter the length of dictionary 1 : "))
for i in range(l1):
    a = input()
    b = input()
    dict1[a] = b

dict2 = {}
l2 = int(input("Enter the length of dictionary 2 : "))
for i in range(l2):
    a = input()
    b = input()
    dict2[a] = b

dict1.update(dict2)
print(dict1)
