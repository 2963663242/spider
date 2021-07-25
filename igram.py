#https://igram.io/en/dl/
import requests
if __name__ == '__main__':
    target_url = "https://igram.io/a/"
    url = "https://www.instagram.com/p/CRMeSWcDeRw/"
    datas = {
        "url": url,
        "lang_code": 'en',
        "csrf_token": 'IjMyM2QwMjdmMTdiMmVmMzQ3MjU0ZDRhNTQ3ZjFkNmM1ZGMyMjNkY2Ui.YP0cEg.0CBxJM7pWv4LdXIcx7fLP_obCEk'
            }
    headers = {
        "sec-ch-ua":'" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile':"?0",
        'Referer':"https://igram.io/en/dl/",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        "cookie": '_ga=GA1.2.1600525491.1627200032; _gid=GA1.2.1871866814.1627200032; _gat_UA-174582130-1=1; __cf_bm=79504ce809dbc39027f53e16e055eea0ce6a41be-1627200032-1800-AfUGMJkDtfNhnUE2000sNwt+3pCQBT7w935G+ATC9M+VEApoP1gbhg6sLPzUFGx7pJ7CSFw0jJR5zYcGAsbnFqJxAIA0DXRAYr4HkcDDQ15JNoTQmvQa2WNsMCBuU0BxhQ==; __gads=ID=a7e3da6a95b4d606-229d4c5889ca001c:T=1627200032:RT=1627200032:S=ALNI_MbqwTYUYwt8YYGxJSt0na_U-Q59ow; session=eyJjc3JmX3Rva2VuIjoiMzIzZDAyN2YxN2IyZWYzNDcyNTRkNGE1NDdmMWQ2YzVkYzIyM2RjZSJ9.YP0aLQ.HJeU2fQ6MplnF_4Iou46hPARG4c; __cflb=02DiuHm6A27GfYCRLCu9CfwynuL92Y7TGHrwKjmnC52R2'
        }
    #proxy = { 'http': ""}
    response = requests.post(url=target_url, headers=headers, data=datas)
    text = response.text
    with open("igram.txt","w") as fp:
        fp.write(text)
    print(text)