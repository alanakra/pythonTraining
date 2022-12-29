def divisible_by_five(el):
    print("Given list is "+str(el))
    print("Divisible by 5")
    for item in el:
        if item % 5 == 0:
            print(item)

x = [10, 20, 33, 46, 55]
divisible_by_five(x)