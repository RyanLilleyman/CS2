'''
nlp spell check testing
'''
from textblob import Word, TextBlob
word = Word('theyr')
print(word.spellcheck())
print(word.correct())

sentence = TextBlob('Ths sentense has missplled wrds.')
print(sentence.correct())