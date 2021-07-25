import requests



if __name__ == '__main__':
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
               }
    url = 'https://worker.sf-tools.com/savefrom.php'
    datas={"sf_url": "https://www.youtube.com/watch?v=O5dvU4o2X8A",
           "sf_submit:": "",
           "new": "2",
           "lang": "en",
           "app": "",
           "country": "hk",
           "os": "Windows",
           "browser": "Chrome",
           "channel": "main",
           "sf-nomad": "1",
           }
    response = requests.post(url=url,headers=headers,data=datas)
    js = response.text
    with open("responese_text.txt","w") as fp:
        fp.write(js)
    print(js)



