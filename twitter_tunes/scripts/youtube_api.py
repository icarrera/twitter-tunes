# coding=utf-8
from apiclient.discovery import build
from apiclient.errors import HttpError
import os
from httplib2 import ServerNotFoundError


YOUTUBE_DEVELOPER_KEY = os.environ.get('YT_AUTH')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
TERMS = ['remix', 'music', 'song', 'parody', 'jam', 'dance']


def youtube_search(keyword, max_results=20):
    """Query YouTube API for search results based off keyword search."""
    try:
        youtube = build(
            YOUTUBE_API_SERVICE_NAME,
            YOUTUBE_API_VERSION,
            developerKey=YOUTUBE_DEVELOPER_KEY
            )
        search_response = youtube.search(
        ).list(
                q=keyword + ' music',
                type='video',
                part='id,snippet',
                maxResults=max_results).execute()
        return search_response
    except HttpError as err:
        print('An HTTP error has occurred.  Please check YT authorization.')
        return err
    except ServerNotFoundError:
        print('Server not found.  Please connect and try again.')
        raise ServerNotFoundError
    except TypeError:
        print('Keyword must be a string.')
        raise TypeError


def youtube_parse(search_result):
    """Parse the YouTube search result to output video ID tag."""
    video_id_uris = []
    try:
        search_items = search_result.get('items', [])
        for result in search_items:
            video_id = result['id']['videoId']
            video_channel = result['snippet']['channelTitle']
            video_title = result['snippet']['title']
            video_id_uris.append((video_id, video_channel, video_title))
        return video_id_uris
    except AttributeError:
        return video_id_uris


def term_checker(title):
    for term in TERMS:
        if term in title.lower():
            return True
    return False


def url_gen(video_id):
    yt_path = 'https://www.youtube.com/'
    yt_uri = 'watch?v=' + video_id
    yt_url = yt_path + yt_uri
    return yt_url


def generate_youtube_link(parsed_list):
    """Generate a youtube video link from parsed list of YouTube video IDs."""
    try:
        for video in parsed_list:
            if 'VEVO' in video[1]:
                return (url_gen(video[0]), True)
        for video in parsed_list:
            if term_checker(video[2]):
                return (url_gen(video[0]), True)
        return (url_gen(parsed_list[0][0]), False)
    except IndexError:
        return (url_gen('b_ILDFp5DGA'), False)


def get_link(trend):
    """Get the single link from the entered trend."""
    return generate_youtube_link(youtube_parse(youtube_search(trend)))
