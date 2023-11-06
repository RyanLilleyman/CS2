'''
Testing Blobs, and dataframes from pd
'''

from pathlib import Path
from operator import itemgetter
from textblob import TextBlob
from nltk.corpus import stopwords



import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# print(text.capitalize())
# print(text.center(20))

blob = TextBlob(Path('/home/ryanlilleyman/repos/CS2/weeks/week9/story.txt').read_text(encoding='utf-8'))
# print(blob.ngrams(2))
# print()
stop_words = stopwords.words('english')
items = blob.word_counts.items()
items = [item for item in items if item[0] not in stop_words]
print(items)
sorted_items = sorted(items,key=itemgetter(1),reverse=True)
top20 = sorted_items[0:21]
df = pd.DataFrame(top20,columns=["Word","Count"])
print(df)

