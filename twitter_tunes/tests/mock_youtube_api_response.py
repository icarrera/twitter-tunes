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
                    'description': "'Purpose' Available Everywhere Now!",
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
                    'title': 'dummy title'}}],
    'kind': 'youtube#searchListResponse',
    'nextPageToken': 'CAoQAA',
    'pageInfo': {
        'resultsPerPage': 10, 'totalResults': 1000000},
    'regionCode': 'US'}

HTTPERROR_RESP = {
    'content-type': 'application/json; charset=UTF-8',
    'x-frame-options': 'SAMEORIGIN',
    'status': '400',
    'x-xss-protection': '1; mode=block',
    'x-content-type-options': 'nosniff',
    'cache-control': 'private, max-age=0',
    'alt-svc': 'quic=":443"; ma=2592000; v="31,30,29,28,27,26,25"',
    'transfer-encoding': 'chunked',
    'expires': 'Tue, 29 Mar 2016 20:03:06 GMT',
    'server': 'GSE', 'vary': 'Origin, X-Origin',
    '-content-encoding': 'gzip', 'alternate-protocol': '443:quic,p=1',
    'date': 'Tue, 29 Mar 2016 20:03:06 GMT',
    'content-length': '176'}

HTTPERROR_CONT = b'{\n "error": {\n  "errors": [\n   {\n    "domain":'
' "usageLimits",\n    "reason": "keyInvalid",\n    "message": "Bad'
' Request"\n   }\n  ],\n  "code": 400,\n  "message": "Bad Request"\n }\n}\n'
