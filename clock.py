from apscheduler.schedulers.blocking import BlockingScheduler
from twitter_tunes.scripts import twitter_bot
from twitter_tunes.redis import redis_data
from twitter_tunes.scripts import twitter_api
import logging

logging.basicConfig()
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=60)
def timed_job():
    twitter_bot.main()


# @sched.scheduled_job('interval', minutes=9)
# def timed_job_redis():
#     trend_list = twitter_api.call_twitter_api()
#     redis_data.set_redis_trend_list(trend_list)


sched.start()
