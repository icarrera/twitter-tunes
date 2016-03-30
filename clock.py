from apscheduler.schedulers.blocking import BlockingScheduler
from twitter_tunes.scripts import twitter_bot
from twitter_tunes.redis import redis
# from twitter_tunes.twitter_api import twitter_api
import logging

logging.basicConfig()
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=60)
def timed_job():
    twitter_bot.main()


@sched.scheduled_job('interval', minutes=9)
def timed_job_redis():
    redis.set_redis_trend_list()


sched.start()
