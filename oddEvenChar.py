# https://pynative.com/python-basic-exercise-for-beginners/

def oddEvenChar():
 inpt = input('Entrez un mot :')
 print('Orginal String is ' + str(inpt))

 for x in range(0, len(inpt)):
  if x % 2 == 0:
   print(inpt[x])

oddEvenChar()
