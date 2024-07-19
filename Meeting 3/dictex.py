fruits = ['apple','banana','melon','grape','apple','apple','banana']

# how many occurences
mydict = {}
for fruits in fruits:
    if fruits in mydict:
        mydict[fruits] += 1
    else:
        mydict[fruits] = 1

    print(mydict)