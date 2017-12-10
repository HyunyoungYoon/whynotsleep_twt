from preprocess_json import get_json
# import kmr_analysis
from konlpy.tag import *
from konlpy.utils import pprint


d = get_json('rawstream2.json')

# print(d[0]['day'])

#naive bayes classifier + smoothing
def naive_bayes_classifier(test, train, all_count):
    counter = 0
    list_count = []
    for i in test:
        for j in range(len(train)):
            if i == train[j]:
                counter = counter + 1
        list_count.append(counter)
        counter = 0
    list_naive = []
    for i in range(len(list_count)):
        list_naive.append((list_count[i]+1)/float(len(train)+all_count))
    result = 1
    for i in range(len(list_naive)):
        result *= float(round(list_naive[i], 6))
    return float(result)*float(1.0/3.0)

kkma = Kkma()
f_pos = open('data/positive.txt', 'r')
f_neg = open('data/negative.txt', 'r')
f_neu = open('data/neutral.txt', 'r')

# tag list (보통명사, 동사, 형용사, 보조동사, 명사추정범주)
# 참고 : https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8/edit#gid=0
list_tag = [u'NNG', u'VV', u'VA', u'VXV', u'UN']
list_positive=[]
list_negative=[]
list_neutral=[]

twt = d[0]['text']
tagged_twt = kkma.pos(twt)
print(tagged_twt)

f_pos.close()
f_neg.close()
f_neu.close()
