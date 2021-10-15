import requests
import json

keyword = input('검색어를 입력하세요: \n')

headers = {
    'authority': 'search.shopping.naver.com',
    'method': 'GET',
    'path': '/search/all?sort=review&pagingIndex=1&pagingSize=40&viewType=list&productSet=total&deliveryFee=&deliveryTypeValue=&frm=NVSHATC&query=%EB%85%B8%ED%8A%B8%EB%B6%81&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&iq=&eq=&xq=',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=UXZGAVUR43SWA; nx_ssl=2; sus_val=Egnhz0odgtmdjqFdO9P+FKGk; SHP_BID=0; spage_uid=; AD_SHP_BID=17',
    'logic': 'PART',
    'referer': 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&pagingIndex=1&pagingSize=40&productSet=total&query=%EB%85%B8%ED%8A%B8%EB%B6%81&sort=date&timestamp=&viewType=list',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'urlprefix': '/api',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

params = (
    ('sort', 'review'),
    ('pagingIndex', '1'),
    ('pagingSize', '40'),
    ('viewType', 'list'),
    ('productSet', 'total'),
    ('deliveryFee', ''),
    ('deliveryTypeValue', ''),
    ('frm', 'NVSHATC'),
    ('query', keyword),
    ('origQuery', keyword),
    ('iq', ''),
    ('ex', ''),
    ('xq', ''),
)

response = requests.get('https://search.shopping.naver.com/search/all', headers=headers, params=params)

result = json.loads(response.text)

# print(result.keys())
# print(result['shoppingResult'].keys())
result_contents = result['shoppingResult']['products']

for content in result_contents:
    print(content['productTitle'])