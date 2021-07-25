import requests



if __name__ == '__main__':
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
               }
    url = 'https://fanyi.baidu.com/'
    response = requests.get(url=url,headers=headers)
    source_page = response.text
    print(source_page)


