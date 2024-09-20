import requests
import re
def gethtml(e):
    print('程序已启动\n正在为您查询数据，请稍后'.center(30))
    url = 'https://osu.ppy.sh/users/%s'%e
    response=requests.get(url=url)
    print(response)
    response.encoding = 'utf-8'
    Osu_html=response.text.replace('&quot;', '"').replace('/','')
    return Osu_html
