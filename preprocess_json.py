import json
from pprint import pprint

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
        #
        twt['day'] = twt['created_at'][:3]
        twt['dd'] = twt['created_at'][8:10]
        twt['hh'] = twt['created_at'][11:13]

        # 원트윗인지 리트윗인지 구분 원트윗이라면 original = 1
        if 'RT' in twt['text'][:3]:
            twt['original'] = 0
        else:
            twt['original'] = 1

    return json_data
