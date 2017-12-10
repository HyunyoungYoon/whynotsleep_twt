from preprocess_json import get_json
from kmr_analysis import *
import pandas as pd

d = get_json('rawstream2.json')

# hh의 종류를 오름차순으로 정리한다
unique_hh = set([twt['hh'] for twt in d])
unique_hh = sorted(list(unique_hh))

for hh in unique_hh:
    # hh 하나에 해당되는 json 전체
    hh_list = list(filter(lambda twt: twt['hh']==hh, d))
    # hh 하나에 해당되는 트윗내용들
    twts = [twt['text'] for twt in hh_list]
    tagged = get_tagged(twts)
    get_wordcloud(tagged)
