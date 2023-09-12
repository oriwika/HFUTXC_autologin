import requests

url = 'http://172.18.3.3/0.htm'

data = {
    "DDDDD": "你的校园网账号",
    "upass": "你的校园网密码",
    "0MKKey": "%B5%C7+%C2%BC%A1%A1Login",
    "v6ip": ""
}
conn=requests.post(url=url,data=data)
