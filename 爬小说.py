import li
import requests

from lxml import etree

url1 = 'https://www.85xs.cc/book/douluodalu1/1.html'
while True:

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

    response = requests.get(url1,headers=headers)

    response.encoding = 'utf-8'

#print(response.text)

    e = etree.HTML(response.text)

    info = '\n'.join(e.xpath('//div[@class="m-post"]/p/text()'))

    title = e.xpath('//h1/text()')[0]

    # url1 = e.xpath('//*[@id="content"]/div[1]/ul/li[2]/a')[0]
    url1 = f'https://www.85xs.cc{e.xpath("//tr/td[2]/a/@href")[0]}'

    with open('斗罗大陆我的爹.txt', 'a', encoding='utf-8') as f:
        f.write(title+'\n\n'+info+'\n\n')

    if url1 == '/book/douluodalu1/1.html':
        break

    # reponser2 = requests.get(url1,headers=headers)
