def treePatern(el):
    for num in range(el+1):
        for i in range(num):
            print(num, end=" ")
        print("\n")

print(treePatern(5))