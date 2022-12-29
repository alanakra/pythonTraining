def isEvenPlace():
    string_name = input("Enter Name:")
    for i in range(len(string_name)):
        if(i%2 == 0):
            print(string_name[i])


isEvenPlace()