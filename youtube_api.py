# coding=utf-8
from apiclient.discovery import build
from apiclient.errors import HttpError
import os


YOUTUBE_DEVELOPER_KEY = os.environ.get('YT_AUTH')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(keyword, max_results=10):
    """Query YouTube API for search results based off keyword search."""
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


def youtube_parse(search_result):
    """Parse the YouTube search result to output video ID tag."""
    try:
        search_items = search_result.get('items', [])
        video_ids = []
        for result in search_items:
            if result['id']['kind'] == 'youtube#video':
                video_ids.append(result['id']['videoId'])
        return video_ids
    except AttributeError:
        print('No YouTube search result detected.')


def generate_youtube_link(parsed_list):
    """Generate a youtube video link from parsed list of YouTube video IDs."""
    top_result = parsed_list[0]
    yt_loc = 'https://www.youtube.com/'
    yt_uri = 'watch?v=' + top_result
    yt_url = yt_loc + yt_uri
    return yt_url
