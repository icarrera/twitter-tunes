# coding=utf-8


BAD_YOUTUBE_RESPONSE = {
    'etag': '"T50iqLU0cleWH2-8bQxaAS2DFh8/ZBV2w65lgyrdAoPQHuFS1_5SrKo"',
    'items': [],
    'kind': 'youtube#searchListResponse',
    'pageInfo': {'resultsPerPage': 10, 'totalResults': 0},
    'regionCode': 'US'}


GOOD_YOUTUBE_RESPONSE = {
    'etag': '"T50iqLU0cleWH2-8bQxaAS2DFh8/rMPhXgkWK6D1tkOLoK27as-vPT0"',
    'items': [{
        'etag': '"T50iqLU0cleWH2-8bQxaAS2DFh8/t65EExZHRMS3i9EoE2pFIrSUw7M"',
        'id': {'kind': 'youtube#video', 'videoId': 'oyEuk8j8imI'},
        'kind': 'youtube#searchResult',
        'snippet': {'channelId': 'UCHkj014U2CQ2Nv0UZeYpE_A',
                    'channelTitle': 'JustinBieberVEVO',
                    'description': "'Purpose' Available Everywhere Now! iTunes: http://smarturl.it/PurposeDlx?IQid=VEVO1113 Stream & Add To Your Spotify Playlist: http://smarturl.it/sPurpose?",
                    'liveBroadcastContent': 'none',
                    'publishedAt': '2015-11-14T15:00:01.000Z',
                    'thumbnails': {
                        'default': {
                            'height': 90,
                            'url': 'https://i.ytimg.com/vi/'
                                   'oyEuk8j8imI/default.jpg',
                            'width': 120},
                        'high': {
                            'height': 360,
                            'url': 'https://i.ytimg.com/vi/'
                                   'oyEuk8j8imI/hqdefault.jpg',
                            'width': 480},
                        'medium': {
                            'height': 180,
                            'url': 'https://i.ytimg.com/vi/'
                                   'oyEuk8j8imI/mqdefault.jpg',
                            'width': 320}},
                    'title': 'Justin Bieber - Love Yourself  '
                             '(PURPOSE : The Movement)'}}],
    'kind': 'youtube#searchListResponse',
    'nextPageToken': 'CAoQAA',
    'pageInfo': {
        'resultsPerPage': 10, 'totalResults': 1000000},
    'regionCode': 'US'}
