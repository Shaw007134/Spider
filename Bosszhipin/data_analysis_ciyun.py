from wordcloud import WordCloud, ImageColorGenerator
from collections import Counter
import json
import pygal
import jieba
import numpy as np
from scipy import stats
from scipy.misc import imread
import pandas as pd
import re
import matplotlib.pyplot as plt

test = []
for line in open('bosszhipin2.txt', 'rb'):
  test.extend(json.loads(line,encoding="latin1"))

post_ul = []
for i in test:
  post = i['post_ul']
  post_ul.append(post)

pattern = re.compile(r'[\u4e00-\u9fa5_a-zA-Z0-9]+')
post_ul = re.findall(pattern, str(post_ul))
post_ul = ' '.join(post_ul)
post_ul = jieba.lcut(str(post_ul),cut_all=False)
post_ul = filter(lambda post_ul: post_ul != ' ', post_ul)
post_ul = list(post_ul)
words_df = pd.DataFrame({'segment':post_ul})

stopwords = pd.read_csv('stopwords.txt',names=['stopword'],encoding='utf-8')

words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

words_stat = words_df.groupby(['segment'])['segment'].agg({'计数':np.size})
words_stat = words_stat.reset_index().sort_values(['计数'],ascending=False)
print(words_stat)

img_mask = imread('brain1.png')
wordcloud = WordCloud(font_path="simhei.ttf",
              background_color = "white",
              max_words = 100,
              mask = img_mask,
              max_font_size = 100,
              random_state = 42
            )
word_freq = {x[0]:x[1] for x in words_stat.head(100).values}

wordcloud.generate_from_frequencies(word_freq)
img_colors = ImageColorGenerator(img_mask)
wordcloud.recolor(color_func=img_colors)

wordcloud.to_file('Word-Cloud-Freq.png')
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
  