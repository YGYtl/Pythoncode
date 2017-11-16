mport requests
from bs4 import BeautifulSoup

resp = requests.get("http://tieba.baidu.com/f?kw=%E5%BF%AB%E4%B9%90%E5%A4%A7%E6%9C%AC%E8%90%A5")
soup = BeautifulSoup(resp.content, 'lxml')

items = soup.find_all('div', 't_con cleafix')

for item in items:
    title_div = item.find('div', 'threadlist_title pull_left j_th_tit ')
    if title_div is not None:
        title = title_div.a.get_text()
    name_div = item.find('div', 'threadlist_author pull_right')
    name = name_div.span.get_text()
    print(title, name)

