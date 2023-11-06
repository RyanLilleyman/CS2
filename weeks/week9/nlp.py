'''
nlp testing
'''
from pathlib import Path
from textblob import TextBlob

neutral_blob = TextBlob(Path('/home/ryanlilleyman/repos/CS2/weeks/week9/story.txt').read_text(encoding=('utf-8')))
positive_blob = TextBlob(Path('/home/ryanlilleyman/repos/CS2/weeks/week9/positive_story.txt').read_text(encoding=('utf-8')))
negative_blob = TextBlob(Path('/home/ryanlilleyman/repos/CS2/weeks/week9/negative_story.txt').read_text(encoding=('utf-8')))
spanish_blob = TextBlob(Path('/home/ryanlilleyman/repos/CS2/weeks/week9/spanish_story.txt').read_text(encoding=('utf-8')))


print(neutral_blob.sentences,end='\n\n')
print(neutral_blob.words,end='\n\n')
print(neutral_blob.tags,end='\n\n')
print(neutral_blob.noun_phrases,end='\n\n')
print(neutral_blob.sentiment,end='\n\n')
print(positive_blob.sentiment,end='\n\n')
print(negative_blob.sentiment,end='\n\n')

for sentence in neutral_blob.sentences:
    print(sentence.sentiment.polarity)

print()
# print(spanish_blob.detect_language(),end='\n\n')
# print(neutral_blob.detect_language(),end='\n\n')

spanish_blob_text = str(spanish_blob)
translated_blob = spanish_blob_text.translate('en')
print(translated_blob, end='\n\n')
