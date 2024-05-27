#https://pynative.com/python-basic-exercise-for-beginners/


def multSum(num1, num2):
 prod = num1 * num2
 sum = num1 + num2
 if (num1 + num2 <= 1000): 
  return sum
 else:
  return prod

print('The result is ' + str(multSum(299399, 294)))
