def hideDuplicate(list):
    newList = []
    for item in list:
        if item not in newList:
            newList.append(item)
    return(newList)

print(hideDuplicate([1,2,2,4,10,6,2,1,3,7,8,10]))