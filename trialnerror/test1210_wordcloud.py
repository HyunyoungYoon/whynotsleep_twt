from preprocess_json import get_json
from kmr_analysis import *
import pandas as pd

d = get_json('rawstream2.json')
d = list(filter(lambda twt: twt['original']==1, d))

# sibal = list(filter(lambda twt: '시발' in twt['text'], d))
# print(len(sibal))
# sibal_twt = [twt['text'] for twt in sibal]
# sibal_tagged = get_tagged(sibal_twt)
# # get_wordcloud(sibal_tagged)
# get_graph(sibal_tagged)

# hh의 종류를 오름차순으로 정리한다
unique_hh = set([twt['hh'] for twt in d])
unique_hh = sorted(list(unique_hh))
unique_day = ['Thu','Fri']

# day,hh에 따른 빈도수
for day in unique_day:
    original_d = list(filter(lambda twt: twt['original']==1, d))
    dd_list = list(filter(lambda twt: twt['day']==day, original_d))
    for hh in unique_hh:
        # hh 하나에 해당되는 json 전체
        hh_list = list(filter(lambda twt: twt['hh']==hh, dd_list))
        # hh 하나에 해당되는 트윗내용들
        # twts = [twt['text'] for twt in hh_list]
        # tagged = get_tagged(twts)
        # get_wordcloud(tagged)
        print(day, hh, len(hh_list))
