dict={'emma':'22','roz':'11','john':'1','alice':'90','rook':'45'}
print("ascending")
print('sorted by key:',sorted(dict.items()))
print('sorted by value:',sorted(dict.items(),key=lambda item:item[1]))
print("descending")
print('sorted by key:',sorted(dict.items(),reverse=True))
print('sorted by value:',sorted(dict.items(),key=lambda item:item[1],reverse=True))

