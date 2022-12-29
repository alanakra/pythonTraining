def check_Palindrome(el):
    reverseNumber = str(el)[::-1]
    print(el, reverseNumber)
    if(el == reverseNumber):
        return "Yes. given number is palindrome number"
    else:
        return "No. given number is not palindrome number"

print(check_Palindrome(125))
print(check_Palindrome(121))
