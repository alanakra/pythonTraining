def multOrSum (num1, num2):
    product = num1*num2
    sum = num1+num2
    if product <= 1000:
        return(product)
    else:
        return(sum)

result = multOrSum(40,30)
print("The result is",result)