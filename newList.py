# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
def new_list(elem1, elem2):
    result_list = []
    
    for i in elem1:
        if i%2 != 0:
            result_list.append(i)
    for i in elem2:
        if i%2 == 0:
            result_list.append(i)
    
    return result_list



list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print(new_list(list1,list2))
