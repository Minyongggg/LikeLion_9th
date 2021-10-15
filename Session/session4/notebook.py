import requests
from bs4 import BeautifulSoup
import csv

file = open( 'notebook.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["상품 제품명", "상품 가격", "상품 상세설명"])

# 우리가 정보를 얻고 싶어 하는 URL
NOTEBOOK_URL = f'https://search.shopping.naver.com/search/all?pagingIndex=1&pagingSize=80&query=노트북'
# get 요청을 통해 해당 페이지 정보를 저장
notebook_html = requests.get(NOTEBOOK_URL)
# bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
notebook_soup = BeautifulSoup(notebook_html.text,"html.parser")

notebook_list_box = notebook_soup.find('ul', {'class':'list_basis'})
notebook_items = notebook_list_box.find_all('li', {'class':'basicList_item__2XT81'})


final_result = []
for notebook_item in notebook_items:

    title = notebook_item.find("a", {'class':'basicList_link__1MaTN'}).text
    price = notebook_item.find("span", {'class':'price_num__2WUXn'}).text
    detail_list = notebook_item.find("div", {'class':'basicList_detail_box__3ta3h'}).find_all("a", {'class':'basicList_detail__27Krk'})

    for i in range(len(detail_list)):
        detail_list[i] = detail_list[i].text
        

    result = {
        'title' : title,
        'price' : price,
        'detail' : detail_list
    }

    final_result.append(result)

for result in final_result:
    row = []
    row.append(result["title"])
    row.append(result["price"])
    row.append(result["detail"])
    writer.writerow(row)



