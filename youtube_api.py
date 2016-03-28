# coding=utf-8
from apiclient.discovery import build
from apiclient.errors import HttpError
import os


YOUTUBE_DEVELOPER_KEY = os.environ.get('YT_AUTH')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(keyword, max_results=10):
    try:
        youtube = build(
            YOUTUBE_API_SERVICE_NAME,
            YOUTUBE_API_VERSION,
            developerKey=YOUTUBE_DEVELOPER_KEY
            )

        search_response = youtube.search(
        ).list(
                q=keyword,
                part='id,snippet',
                maxResults=max_results).execute()
        return search_response
    except HttpError:
        print('An HTTP error has occurred.')
