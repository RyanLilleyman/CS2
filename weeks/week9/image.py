'''
Word Cloud Test
'''
from pathlib import Path
from wordcloud import WordCloud
import imageio
text = Path('/home/ryanlilleyman/repos/CS2/weeks/week9/story.txt').read_text(encoding=('utf-8'))
mask_image = imageio.imread('/home/ryanlilleyman/repos/CS2/weeks/week9/heart.png')
wordcloud = WordCloud(width=1000, height=1000,
colormap='prism', mask=mask_image, background_color='white')
wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file('test.png')

