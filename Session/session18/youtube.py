import json
import requests
# results?search_query=% 의 request headers 파트에서 확인
headers = {
'x-youtube-client-name': '1',
'x-youtube-client-version': '2.20210708.06.00'
}
# url ? 뒤에 들어가는 parameter
# results?search_query=% 의 query string parameters 파트에서 확인
params = (
('search_query', input('검색어를 입력하세요 : \n')),
('pbj', '1')
)
# 검색어 입력했을 때 url
# results?search_query=% 의 general 파트의 request url
response = requests.get('https://www.youtube.com/results', headers=headers, params=params)
result = json.loads(response.text)
contents = result[1]['response']['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']

# 검색된 영상들의 videoId 값들을 videoId_list에 저장
videoId_list = []
for content in contents:
    keys = list(content.keys())
    if 'videoRenderer' in keys:
        videoId_list.append(content['videoRenderer']['videoId'])

print(videoId_list)


for videoId in videoId_list:
    print("-----------------------------------------")
    # video_headers = {
    #     'authority': 'www.youtube.com',
    #     'method': 'POST',
    #     'path': '/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
    #     'scheme': 'https',
    #     'accept': '*/*',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    #     'authorization': 'SAPISIDHASH 1626364075_f3167fe40e3e57c9a8996562c83f8b84bfaf554c',
    #     'content-length': '2300',
    #     'content-type': 'application/json',
    #     'cookie': 'VISITOR_INFO1_LIVE=EtHUmn8u_T8; PREF=f4=4000000&tz=Asia.Seoul; YSC=Bw_-VlXfArA; SID=_weUAxRHTOeZCFdjgnCHk7bsAVUfli_mbfCfRUQ_Y9ghgM24LGNfSpdzFVhuHyinZWiaqA.; __Secure-1PSID=_weUAxRHTOeZCFdjgnCHk7bsAVUfli_mbfCfRUQ_Y9ghgM24zmBobZo_pYRaG85BCHXW4Q.; __Secure-3PSID=_weUAxRHTOeZCFdjgnCHk7bsAVUfli_mbfCfRUQ_Y9ghgM24Rmx9sZ4s0yE_RJo64ChLjQ.; HSID=A04KMUo-jI-qu2SJh; SSID=A3Kl8he7eiTRsQ9yr; APISID=YV2vAnULk9_xrlVU/AfU-VMbt5hLi8isRX; SAPISID=2TFJa49e7LMB1IxI/ABd-bDjoBDCMMlRAF; __Secure-1PAPISID=2TFJa49e7LMB1IxI/ABd-bDjoBDCMMlRAF; __Secure-3PAPISID=2TFJa49e7LMB1IxI/ABd-bDjoBDCMMlRAF; LOGIN_INFO=AFmmF2swRAIgANp54OI9bfWaO5-0Yhyt8vEMn4qLGUr7SUd3bV_h79UCIErEM99sNjtPLVRp7MHjgVlX69h2daW6CH1EwXMVZ_ZG:QUQ3MjNmd1NKT2Y0aEp6cGxyeG4xNk51RThKZnpfb1lvMllPOHk0SDU0WDJubTMtUHlXQVY1X011eVF2REZRZkdfTlFzUHYyY0ExQkpZc3VUMGd5VU5ER0FDcFc3SDM0cWk0dmpCdDJFazNZb3gyMk1aQ3haTFRnZi1jeUxYT3ZYLW5xRzFlb3JEVncyUTg0NHVDMTE1ZUpXbjljcVpIazdB; SIDCC=AJi4QfE-PzR_Osf_c482cXGLc_qb2z9G2w9UUHibUNxYGV8HZ9lwyJfTurPVwrA2D4nuSDnTHA; __Secure-3PSIDCC=AJi4QfF3yPyWnZUlbJFvj4NlIrjSqDfLGP2zoA26GOpHHsV___-NFZ11_Z_cI97DoI7htGjhXA; ST-wy42ea=itct=CIsCENwwGAYiEwjG_cegtuXxAhUNYGAKHWRmAT8yBnNlYXJjaFIJ7JWE7J207JygmgEDEPQk&csn=MC4zMTA1NjY4MTgzMTk1NzI5&endpoint=%7B%22clickTrackingParams%22%3A%22CIsCENwwGAYiEwjG_cegtuXxAhUNYGAKHWRmAT8yBnNlYXJjaFIJ7JWE7J207JygmgEDEPQk%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fwatch%3Fv%3DD1PvIWdJ8xo%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_WATCH%22%2C%22rootVe%22%3A3832%7D%7D%2C%22watchEndpoint%22%3A%7B%22videoId%22%3A%22D1PvIWdJ8xo%22%2C%22params%22%3A%22qgMJ7JWE7J207JygugMLCMiCjp2hg7GFhQG6AwsItZGUvpqlrfXTAboDCwikluf_0cv6m8ABugMLCIeY4qux57nbvwG6AwoIidLwuazPvv5bugMKCLLbn4Cv3IqDM7oDCwivzPmguvrPkd4BugMLCKzZjqGHsbGh2gG6AwsIwc7H8sihzOacAboDCwj-6az6_7aPqv0BugMLCNPJopr8yZTQ8wG6AwoI3-Ca54CQmuI6ugMKCMK8_5i02uuBTroDCwikm4jgrYKPpYcBugMLCMy7rsnqz6iY2gG6AwoI35b6iO-0t4cIugMKCOGl5MqVxa_SDLoDCwiAybjtuauN6J8BugMLCLHioczZt_Ha-wHyAwUNqDtZPg%253D%253D%22%2C%22watchEndpointSupportedOnesieConfig%22%3A%7B%22html5PlaybackOnesieConfig%22%3A%7B%22commonConfig%22%3A%7B%22url%22%3A%22https%3A%2F%2Fr1---sn-qap8x3g-pjol.googlevideo.com%2Finitplayback%3Fsource%3Dyoutube%26orc%3D1%26oeis%3D1%26c%3DWEB%26oad%3D3200%26ovd%3D3200%26oaad%3D11000%26oavd%3D11000%26ocs%3D700%26oewis%3D1%26oputc%3D1%26ofpcc%3D1%26msp%3D1%26odeak%3D1%26odepv%3D1%26osfc%3D1%26ip%3D124.5.155.177%26id%3D0f53ef216749f31a%26initcwndbps%3D962500%26mt%3D1626361560%26oweuc%3D%22%7D%7D%7D%7D%7D',
    #     'origin': 'https://www.youtube.com',
    #     'referer': 'https://www.youtube.com/watch?v=D1PvIWdJ8xo',
    #     'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-fetch-dest': 'empty',
    #     'sec-fetch-mode': 'same-origin',
    #     'sec-fetch-site': 'same-origin',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    #     'x-goog-authuser': '0',
    #     'x-goog-visitor-id': 'CgtFdEhVbW44dV9UOCjCsMGHBg%3D%3D',
    #     'x-origin': 'https://www.youtube.com',
    #     'x-youtube-client-name': '1',
    #     'x-youtube-client-version': '2.20210713.07.00'
    # }
    # video_params = (
    #     ('key', 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8')
    # )






#     # player?key= 의 query string parameters 파트 복붙
#     # 쉼표 주의
    video_params = (
    ('key', 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'),
    )
#     # player?key= 의 request payload 파트 복붙 (view source)
    # videoId 값만 변수로 변경
    video_headers = {
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20210708.06.00'
    }
    data = {
        "videoId":videoId,
        "context":{
            "client":{
                "hl": "ko",
                "gl": "KR",
                "remoteHost": "221.143.13.177",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgtLbWtDR3hqdzEtOCiJqcCHBg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20210713.07.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/watch?v=wDfqXR_5yyQ",
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "timeZone": "Asia/Seoul",
                "browserName": "Chrome",
                "browserVersion": "91.0.4472.124",
                "screenWidthPoints": 539,
                "screenHeightPoints": 716,
                "screenPixelDensity": 1,
                "screenDensityFloat": 1,
                "utcOffsetMinutes": 540,
                "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
                "clientScreen": "WATCH",
                "mainAppWebInfo": {
                    "graftUrl": "/watch?v=wDfqXR_5yyQ",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user":{
                "lockedSafetyMode": False
            },
            "request":{
                "useSsl":True,
                "internalExperimentFlags":[],       
                "consistencyTokenJars":[]
            },
            "adSignalsInfo":{
                "bid":"ANyPxKrzWuvB5JF2P_ysQQY6TNWhGJZpzLsE_PrEdoIqst846L72mFhr68xv8iHwOgO9MIG1do5A_fi781dGhyWeI24dXFlBAQ"
            }
        },
        "playbackContext":{
            "contentPlaybackContext":{
            # 너무 길어서 중간 생략합니다.
            }
        },
        "cpn":"9wbWDn8Kn3B5Yv4s","captionParams":{}
    }
    data = json.dumps(data)
    # player?key= 의 general 파트의 request url
    response = requests.post('https://m.youtube.com/youtubei/v1/player',headers=video_headers, params=video_params, data=data)
    # json 디코딩 (json to python)
    result = json.loads(response.text)
    # player_response = result['streamingData']['formats']
    # for item in player_response:
    #     keys = list(item.keys())
    #     # print(keys)
    #     if 'url' in keys :
    #         print(">>",item['url'])
    player_response = result['streamingData']['formats'][0]
    keys = list(player_response.keys())
    # print(keys)
    if 'url' in keys :
        print(">>",player_response['url'])