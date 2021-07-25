import json
import requests
import datetime

postUrl = 'https://api.y2mate.guru/api/convert'
# payloadData数据
payloadData = {

    "url":"https://www.instagram.com/p/CRl7KMpjPog/"
}
# 请求头设置
payloadHeader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Content-Type': 'application/json',
}
# 下载超时
timeOut = 25
# 代理
proxy = "http://user-proxy02:UkUhCg3ihC@gate.dc.smartproxy.com:20000"
proxies = {
    "http": proxy,
    "https": proxy,
}
r = requests.post(postUrl, data=json.dumps(payloadData), headers=payloadHeader)

dumpJsonData = json.dumps(payloadData)
# print(f"dumpJsonData = {dumpJsonData}")
res = requests.post(postUrl, data=dumpJsonData, headers=payloadHeader, timeout=timeOut,  allow_redirects=True)
# # 下面这种直接填充json参数的方式也OK
# # res = requests.post(postUrl, json=payloadData, headers=header)
print(f"responseTime = {datetime.datetime.now()}, statusCode = {res.status_code}, res text = {res.text}")
# print(r.text)