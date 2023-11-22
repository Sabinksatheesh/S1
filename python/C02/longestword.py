l1=[]
l2=[]
def longest(words):
    l2=[]
    for word in words:
        l2.append((len(word),word))
    l2.sort()
    print("longest word:",l2[-1][1],"\n length:",len(l2[-1][1]))
n=int(input('enter size of l1:'))
print('enter elements of l1:')
for i in range(0,n):
    l1.append(input())
longest(l1)