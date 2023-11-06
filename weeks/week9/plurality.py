'''
nlp plurality testing
'''
from textblob import Word, TextBlob
index = Word('index')
print(index.pluralize())

cacti = Word('cacti')
print(cacti.singularize())

animals = TextBlob('cat dog mouse ox').words
print(animals.pluralize())

