import tweepy
import json
import time
from apscheduler.schedulers.blocking import BlockingScheduler
# https://stackoverflow.com/questions/22715086/scheduling-python-script-to-run-every-hour-accurately


# OAuth setup
consumer_key = '0hjtMavZ9ms2PSeZg4uSMMVEI'
consumer_secret = 'BkvgfITMQf2lgJx5tr8Yd0T6oqHVjv4AgXLtTSb0sRSttgzwaa'
access_token = '930699426829688833-E9auo3HBCqWE4XEnElGc7dQC8yYh6hx'
access_secret = 'R1k0Ny0M2VxinX30LDJmYio7xN4iG4sNFLQ1H0p7w8TX0'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


# https://stackoverflow.com/questions/33498975/unable-to-stop-streaming-in-tweepy-after-one-minute
#json 데이타로 저장
class MyListener(tweepy.StreamListener):
    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit

        # self.day = time.localtime(self.start_time).tm_day
        # self.fileName = 'rawstream' + str(self.day) + '.json'
        # self.saveFile = open(self.fileName, 'a')

        self.saveFile = open('rawstream.json', 'a')
        super(MyListener, self).__init__()


    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            self.saveFile.write(data)
            self.saveFile.write('\n')
            return True
        else:
            self.saveFile.close()
            return False

#스트리밍 시작
# twitter_stream = tweepy.Stream(auth=api.auth, listener=MyListener(time_limit=60))
# twitter_stream.filter(track=['시험','과제','종강','팀플'])


def get_stream():
    #180초=3분씩
    twitter_stream = tweepy.Stream(auth=api.auth, listener=MyListener(time_limit=180))
    twitter_stream.filter(track=['시험','과제','종강','팀플','교수'])

scheduler = BlockingScheduler()
#10분마다
scheduler.add_job(get_stream, 'interval', minutes=10)
scheduler.start()
