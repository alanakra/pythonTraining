def checkSameNum(el):
    first = el[0]
    last = el[-1]
    if first == last:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print("result is", checkSameNum(numbers_x))
print("result is", checkSameNum(numbers_y))