# coding=utf-8


BAD_YOUTUBE_RESPONSE = {
    'etag': '"q5k97EMVGxODeKcDgp8gnMu79wM/ZBV2w65lgyrdAoPQHuFS1_5SrKo"',
    'items': [],
    'kind': 'youtube#searchListResponse',
    'pageInfo': {'resultsPerPage': 10, 'totalResults': 0},
    'regionCode': 'US'
    }


GOOD_YOUTUBE_RESPONSE = {
    'etag': '"q5k97EMVGxODeKcDgp8gnMu79wM/hQDR-Lg0AwIzlAjFoYPw3PDOekk"',
    'items':
        [{'etag': '"q5k97EMVGxODeKcDgp8gnMu79wM/8dnEJZcvm8isZPZXMt_m2T0UfSE"',
          'id': {
            'channelId': 'UCHkj014U2CQ2Nv0UZeYpE_A',
            'kind': 'youtube#channel'
            },
          'kind': 'youtube#searchResult',
          'snippet': {'channelId': 'UCHkj014U2CQ2Nv0UZeYpE_A',
                      'channelTitle': 'JustinBieberVEVO',
                      'description': '',
                      'liveBroadcastContent': 'none',
                      'publishedAt': '2009-09-26T03:46:15.000Z',
                      'thumbnails': {'default': {'url':
          'https://yt3.ggpht.com/-VA1VJBph20Q/AAAAAAAAAAI/AAAAAAAAAAA/WJxOBPTsGt8/s512-c-k-no/photo.jpg'},
          'high': {'url': 'https://yt3.ggpht.com/-VA1VJBph20Q/AAAAAAAAAAI/AAAAAAAAAAA/WJxOBPTsGt8/s512-c-k-no/photo.jpg'},
          'medium': {'url': 'https://yt3.ggpht.com/-VA1VJBph20Q/AAAAAAAAAAI/AAAAAAAAAAA/WJxOBPTsGt8/s512-c-k-no/photo.jpg'}},
          'title': 'JustinBieberVEVO'}}],
          'kind': 'youtube#searchListResponse',
          'nextPageToken': 'CAoQAA',
          'pageInfo': {'resultsPerPage': 10, 'totalResults': 1000000},
          'regionCode': 'US'}
