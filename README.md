# HFUTXC_autologin
##适用于合肥工业大学宣城校区的校园网自动登录

###第一种方式Python
####依赖 requests  ---- (pip install requests)

####下载login.py,修改里面的校园网账号和密码

####然后python执行login.py

###第二种方式bash命令

###bash执行
```bash
curl -i -d 'DDDDD=修改为你的校园网账号&upass=修改为你的校园网密码&0MKKey=%B5%C7+%C2%BC%A1%A1Login&v6ip=' 'http://172.18.3.3/0.htm'
```
