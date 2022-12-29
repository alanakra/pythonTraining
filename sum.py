def sum():
    for i in range(10):
        current = i
        previous = i-1
        if i == 0:
            previous = 0
        sum = i+previous
        print("Current Number "+str(current)+" Previous Number "+str(previous)+" Sum:"+str(sum))


print(sum())