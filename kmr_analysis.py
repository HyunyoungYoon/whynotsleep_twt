# https://grahamnic.wordpress.com/2013/09/15/python-using-the-twitter-api-to-datamine/
# import twitter
from konlpy.tag import Komoran
from collections import Counter
from wordcloud import WordCloud
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# api = twitter.Api(
#  consumer_key='Xaf3MZWMyaVBbPxNXvDF4YAzO',
#  consumer_secret='o6oFol3eHPduN9f4ZNOMjgqo0NXs40JM5dvnzFF4N249fn17Ae',
#  access_token_key='1650621372-NmDH5lZi3TkoFdsp01WZRbQcRA9fMyhqAcBdKjR',
#  access_token_secret='amduGj28nOmEPNbgoaaAf73reqqW7OpEN3BuhW0cGmSRz'
#  )

# 낙태법 폐지 청원에 대한 조국 수석의 답변을 기준으로 낙태에 대한 트윗을 수집한다.
# until = api.GetSearch(term='낙태', until='2017-11-26', count=100)
# since = api.GetSearch(term='낙태', since='2017-11-27', count=100)

# 트윗에서 트윗의 내용만 뽑아낸다
# utext=[]
# stext=[]
# for model in until:
#     utext.append(model.text)
# for model in since:
#     stext.append(model.text)


# 단어 태그하기
# sentences(리스트) 입력시 (word, tag)순서쌍 리스트의 리스트 반환
def get_tagged(sentences):
    tagger = Komoran()
    return [tagger.pos(sent) for sent in sentences]


# 명사의 빈도수 리스트
def count_noun(tagged):
    noun_list = []
    for twt in tagged:
        for word, tag in twt:
            if tag in ['NNP', 'NNG']:
                noun_list.append(word)
    noun_counts = Counter(noun_list)
    return noun_counts

def get_wordcloud(tagged):
    noun_counts = count_noun(tagged)

    cloud = WordCloud(width=400, height=300,
                      font_path='data/08seoulnamsan B 2.ttf',
                      background_color='white')
    cloud = cloud.fit_words(noun_counts)

    fig = plt.figure(figsize=(10, 10))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()


# 태그된 트윗 리스트를 넣으면 등장한 명사들의 고유 리스트를 반환
def get_unique(tagged):
    unique_nouns = set()
    for twt in tagged:
        for word, tag in twt:
            if tag in ['NNP', 'NNG']:
                unique_nouns.add(word)
    unique_nouns = list(unique_nouns)
    return unique_nouns


# 고유한 명사를 key로, 그에 매긴 번호를 value로 하는 딕셔너리 반환
def get_noun_index(unq):
    noun_index = {noun: i for i, noun in enumerate(unq)}
    return noun_index


# 문장-단어 행렬, 공존행렬 만들기
def get_occur(tagged):
    unq = get_unique(tagged)
    noun_index = get_noun_index(unq)

    occurs = np.zeros([len(tagged), len(unq)])
    for i, twt in enumerate(tagged):
        for word, tag in twt:
            if tag in ['NNP', "NNG"]:
                index = noun_index[word]
                occurs[i][index] = 1
    co_occurs = occurs.T.dot(occurs)
    return co_occurs

def get_graph(tagged):
    unq = get_unique(tagged)
    co_occurs = get_occur(tagged)
    graph = nx.Graph()
    for i in range(len(unq)):
        for j in range(i + 1, len(unq)):
            if co_occurs[i][j] > 1: #기준 완화
                graph.add_edge(unq[i], unq[j])

    plt.figure(figsize=(15, 15))
    layout = nx.spring_layout(graph, k=.1)
    nx.draw(graph, pos=layout, with_labels=True,
            font_size=10, font_family="AppleGothic",
            alpha=0.3, node_size=2000)
    plt.show()
