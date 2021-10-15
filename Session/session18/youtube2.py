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

print(result)

# contents = result[1]['response']['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']
# # 검색된 영상들의 videoId 값들을 videoId_list에 저장
# videoId_list = []
# for content in contents:
#     keys = list(content.keys())
#     if 'videoRenderer' in keys:
#         videoId_list.append(content['videoRenderer']['videoId'])
# print(videoId_list)