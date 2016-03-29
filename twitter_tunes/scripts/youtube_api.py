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
    except HttpError as err:
        print('An HTTP error has occurred.')
        return err


def youtube_parse(search_result):
    """Parse the YouTube search result to output video ID tag."""
    video_id_uris = []
    try:
        search_items = search_result.get('items', [])
        for result in search_items:
            if result['id']['kind'] == 'youtube#video':
                video_id = result['id']['videoId']
                video_channel = result['snippet']['channelTitle']
                video_id_uris.append((video_id, video_channel))
        return video_id_uris
    except AttributeError:
        return video_id_uris


def generate_youtube_link(parsed_list):
    """Generate a youtube video link from parsed list of YouTube video IDs."""
    yt_path = 'https://www.youtube.com/'
    try:
        for video in parsed_list:
            if 'VEVO' in video[1]:
                top_result = video[0]
                yt_uri = 'watch?v=' + top_result
                yt_url = yt_path + yt_uri
                return yt_url
        top_result = parsed_list[0][0]
        yt_uri = 'watch?v=' + top_result
        yt_url = yt_path + yt_uri
        return yt_url
    except IndexError:
        top_result = 'b_ILDFp5DGA'
        yt_uri = 'watch?v=' + top_result
        yt_url = yt_path + yt_uri
        return yt_url


def get_link(trend):
    """Get the single link from the entered trend."""
    return generate_youtube_link(youtube_parse(youtube_search(trend)))
