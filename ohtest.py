import json
from pprint import pprint
import tweepy

with open("rawstream2.json","r",encoding='utf-8') as r:
    all_data = r.readlines()

json_data = []

for data in all_data:
    try:
        json_data.append(json.loads(data,encoding='utf-8'))
    except:
        pass

Thr_09 = []
Thr_10 = []
Thr_11 = []
Thr_12 = []
Thr_13 = []
Thr_14 = []
Thr_15 = []
Thr_16 = []
Thr_17 = []
Thr_18 = []
Thr_19 = []
Thr_20 = []
Thr_21 = []
Thr_22 = []
Thr_23 = []

Fri_00 = []
Fri_01 = []
Fri_02 = []
Fri_03 = []
Fri_04 = []
Fri_05 = []
Fri_06 = []
Fri_07 = []
Fri_08 = []
Fri_09 = []
Fri_10 = []
Fri_11 = []
Fri_12 = []
Fri_13 = []
Fri_14 = []
Fri_15 = []
Fri_16 = []
Fri_17 = []
Fri_18 = []
Fri_19 = []
Fri_20 = []
Fri_21 = []
Fri_22 = []
Fri_23 = []

Sat_00 = []
Sat_01 = []
Sat_02 = []
Sat_03 = []
Sat_04 = []
Sat_05 = []
Sat_06 = []
Sat_07 = []
Sat_08 = []

for tweet in json_data :
    if ("ko" in tweet["lang"]) : # 제 컴에서는 자꾸 커널 터져서 부득이하게 넣었습니다. 한국어 트윗만 골라내는거라 이거 생략하셔도 됩니다.
        if "Thu" in tweet["created_at"] :
            if " 09:" in tweet["created_at"] :
                Thr_18.append(tweet['text'])
            elif " 10:" in tweet["created_at"] :
                Thr_19.append(tweet)
            elif " 11:" in tweet["created_at"] :
                Thr_20.append(tweet)
            elif " 12:" in tweet["created_at"] :
                Thr_21.append(tweet)
            elif " 13:" in tweet["created_at"] :
                Thr_22.append(tweet)
            elif " 14:" in tweet["created_at"] :
                Thr_23.append(tweet)
            elif " 15:" in tweet["created_at"] :
                Fri_00.append(tweet['text'])
            elif " 16:" in tweet["created_at"] :
                Fri_01.append(tweet)
            elif " 17:" in tweet["created_at"] :
                Fri_02.append(tweet)
            elif " 18:" in tweet["created_at"] :
                Fri_03.append(tweet)
            elif " 19:" in tweet["created_at"] :
                Fri_04.append(tweet)
            elif " 20:" in tweet["created_at"] :
                Fri_05.append(tweet)
            elif " 21:" in tweet["created_at"] :
                Fri_06.append(tweet)
            elif " 22:" in tweet["created_at"] :
                Fri_07.append(tweet)
            elif " 23:" in tweet["created_at"] :
                Fri_08.append(tweet)
        if "Fri" in tweet["created_at"] :
            if " 00:" in tweet["created_at"] :
                Fri_09.append(tweet)
            elif " 01:" in tweet["created_at"] :
                Fri_10.append(tweet)
            elif " 02:" in tweet["created_at"] :
                Fri_11.append(tweet)
            elif " 03:" in tweet["created_at"] :
                Fri_12.append(tweet)
            elif " 04:" in tweet["created_at"] :
                Fri_13.append(tweet)
            elif " 05:" in tweet["created_at"] :
                Fri_14.append(tweet)
            elif " 06:" in tweet["created_at"] :
                Fri_15.append(tweet)
            elif " 07:" in tweet["created_at"] :
                Fri_16.append(tweet)
            elif " 08:" in tweet["created_at"] :
                Fri_17.append(tweet)
            elif " 09:" in tweet["created_at"] :
                Fri_18.append(tweet)
            elif " 10:" in tweet["created_at"] :
                Fri_19.append(tweet)
            elif " 11:" in tweet["created_at"] :
                Fri_20.append(tweet)
            elif " 12:" in tweet["created_at"] :
                Fri_21.append(tweet)
            elif " 13:" in tweet["created_at"] :
                Fri_22.append(tweet)
            elif " 14:" in tweet["created_at"] :
                Fri_23.append(tweet)
            elif " 15:" in tweet["created_at"] :
                Sat_00.append(tweet)
            elif " 16:" in tweet["created_at"] :
                Sat_01.append(tweet)
            elif " 17:" in tweet["created_at"] :
                Sat_02.append(tweet)
            elif " 18:" in tweet["created_at"] :
                Sat_03.append(tweet)
            elif " 19:" in tweet["created_at"] :
                Sat_04.append(tweet)
            elif " 20:" in tweet["created_at"] :
                Sat_05.append(tweet)
            elif " 21:" in tweet["created_at"] :
                Sat_06.append(tweet)
            elif " 22:" in tweet["created_at"] :
                Sat_07.append(tweet)
            elif " 23:" in tweet["created_at"] :
                Sat_08.append(tweet)

#######################################################

from konlpy.tag import Kkma
from konlpy.tag import Komoran
import random as rd

Thr_18 = [line for line in Thr_18 if line != '']
#print (sentence)
#pos_sentences = [line for line in lines if line[-1] == "1"]
sent = Fri_00[0]

tagger = Komoran()
tags = tagger.pos(sent)

tags
tagged_sentences = [tagger.pos(sent) for sent in Thr_18]


#print(adj_list)

#rd.shuffle(pos_tagged_sentences)
#pos_tagged_sentences2 = pos_tagged_sentences[0:1000]

#tagged_sentences = [tagger.pos(sent) for sent in pos_tagged_sentences2]


noun_list = []
for sent in tagged_sentences:
    for word, tag in sent:
        if tag in ['NNG','NNP']:
            noun_list.append(word)




#for hys in adj_list :
#    hys += '다'
#    adj_list.append(hys)
#adj_list

#from collections import Counter
#adj_counts = Counter(adj_list)
#adj_counts.most_common(100)


from collections import Counter
noun_counts = Counter(noun_list)
noun_counts.most_common(100)


import matplotlib.pyplot as plt
from wordcloud import WordCloud

cloud = WordCloud(width=900, height=600,
                  # font_path='data/08seoulnamsan B.ttf',
                  background_color='white')

cloud = cloud.fit_words(noun_counts)

plt.figure(figsize=(15, 20))
plt.axis('off')
plt.imshow
plt.show()
