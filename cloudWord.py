import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# open file
f = open('text.txt', 'rt')
content = f.read()
words = re.split(r'\s+', content)

# List to_exclude comes from https://datascientest.com/wordcloud-python
to_exclude = ['d', 'du', 'de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
text = ' '.join(words)

wordcloud = WordCloud(width=800, height=400, stopwords=to_exclude, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Masquer les axes
plt.show()

f.close()