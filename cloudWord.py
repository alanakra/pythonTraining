import re

# open file
f = open('text.txt', 'rt')
content = f.read()
split_content = re.split(r'\s+', content)
print(split_content)
f.close()