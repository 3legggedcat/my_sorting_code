
mylist = [2, 4, 6, 3, 7, 8, -7, -10, 50000, 2983659264, 57, 349, 35]
newlist = []
for i in range(len(mylist)):

    x = min(mylist)
    y = mylist.index(x)
    newlist.append(x)
    mylist.pop(y)

print(newlist)
