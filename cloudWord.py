# open file
f = open('text.txt', 'rt')
for x in f:
    if x == 'prince':
        print('prince')
f.close()