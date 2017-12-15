import json
from pprint import pprint
from datetime import datetime, timedelta

def get_json(json_file):

    with open(json_file,"r",encoding='utf-8') as r:
        all_data = r.readlines()

    json_data = []

    for data in all_data:
        try:
            json_data.append(json.loads(data,encoding='utf-8'))
        except:
            pass

    for twt in json_data:
        # created_at datetime object로
        str_date = '2017 12 '+ twt['created_at'][8:19]
        obj_date = datetime.strptime(str_date, '%Y %m %d %H:%M:%S')
        created_at = obj_date + timedelta(hours=9) #시차 계산
        twt['created_at'] = created_at

        # 필터링에 쓰일 attribute 생성
        twt['day'] = twt['created_at'].day
        twt['hh'] = twt['created_at'].hour

        # 원트윗인지 리트윗인지 구분 원트윗이라면 original = 1
        # 확인 필요
        if 'RT' in twt['text'][:3]:
            twt['original'] = 0
        else:
            twt['original'] = 1

    return json_data
