import requests
from bs4 import BeautifulSoup
import  time

def download_page(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("页面下载失败")

def get_pic(html):
    soup=BeautifulSoup(html,'html.parser')
    pic_list=soup.find('ul',class_='list_con_hot_ul').find_all('li')
    pic2_list=(soup.find('ul',class_='list_con_tj_ul').find_all('li'))
    for i in pic2_list:
        pic_list.append(i)
    for i in pic_list:
        img_tag=i.find('img')
        text=img_tag.get('alt')
        pic_link=img_tag.get('src')
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
        r=requests.get(pic_link,headers=header,timeout=30)
        path='E:\Pycharm\PyCharm 2020.1\爬虫实战\妹子图\{}'.format(pic_link.split('/')[-1])
        with open(path, 'wb') as f:
            f.write(r.content)
            time.sleep(1)

def main():
  url='https://www.tupianzj.com/meinv/mm/meizitu/'
  page_html=download_page(url)
  get_pic(page_html)

if __name__=='__main__':
    main()

