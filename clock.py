from apscheduler.schedulers.blocking import BlockingScheduler
from twitter_tunes.scripts import twitter_bot
from twitter_tunes.scripts import redis_data
from twitter_tunes.scripts import twitter_api
import logging

logging.basicConfig()
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=60)
def timed_job():
    """Trigger tweet every hour."""
    print('Time to make a Tweet!...')
    twitter_bot.main()


@sched.scheduled_job('interval', minutes=9)
def timed_job_redis():
    """Update redis every 9 minutes."""
    print('Updating Redis...')
    trend_list = twitter_api.call_twitter_api()
    redis_data.set_redis_trend_list(trend_list)


sched.start()
