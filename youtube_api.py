# coding=utf-8
from apiclient.discovery import build
from apiclient.errors import HttpError
import os


DEVELOPER_KEY = os.environ.get('YT_AUTH')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(keyword):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY)
