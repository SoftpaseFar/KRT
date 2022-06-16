import requests


def certificate():
  r = requests.get('https://www.chsi.com.cn/xlcx/bg.do?vcode=AUBGKX3N00G7H3BC')
  print(r.text)


certificate()
