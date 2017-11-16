from urllib import request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # resp = requests.get("http://big5.quanben5.com/n/dihuang-shenyiqifei/21253.html")
    url = "http://big5.quanben5.com/n/dihuang-shenyiqifei/21253.html"
    # soup = BeautifulSoup(resp.content, 'lxml')
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'

    req = request.Request(url, headers=head)
    response = request.urlopen(req)
    html = response.read()

    soup = BeautifulSoup(html, 'lxml')
    soup_texts = soup.find_all('div', id='content')

    for soup_text in soup_texts:
        print(soup_text.text)


'''
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
'''
'''
模仿。。。
'''