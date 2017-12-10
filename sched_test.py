import tweepy
import json
import time
from apscheduler.schedulers.blocking import BlockingScheduler
# https://stackoverflow.com/questions/22715086/scheduling-python-script-to-run-every-hour-accurately


# OAuth setup
consumer_key = 'Xaf3MZWMyaVBbPxNXvDF4YAzO'
consumer_secret = 'o6oFol3eHPduN9f4ZNOMjgqo0NXs40JM5dvnzFF4N249fn17Ae'
access_token = '1650621372-NmDH5lZi3TkoFdsp01WZRbQcRA9fMyhqAcBdKjR'
access_secret = 'amduGj28nOmEPNbgoaaAf73reqqW7OpEN3BuhW0cGmSRz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


# https://stackoverflow.com/questions/33498975/unable-to-stop-streaming-in-tweepy-after-one-minute
#json 데이타로 저장
class MyListener(tweepy.StreamListener):
    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('timetest60.json', 'a')
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
    twitter_stream = tweepy.Stream(auth=api.auth, listener=MyListener(time_limit=300))
    twitter_stream.filter(track=['시험','과제','종강','팀플','교수'])

scheduler = BlockingScheduler()
scheduler.add_job(get_stream, 'interval', minutes=30)
scheduler.start()
