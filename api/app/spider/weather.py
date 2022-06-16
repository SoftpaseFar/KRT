import requests
from flask import current_app


def get_weather(latitude, longitude):
  # 请求url
  host = 'https://jisutqybmf.market.alicloudapi.com'
  path = '/weather/query'
  query = 'location=' + str(latitude) + ',' + str(longitude)

  url = host + path + '?' + query


  # header构建
  appcode = current_app.config["APPCODE"]

  headers = {
    'Authorization': 'APPCODE ' + appcode,
    'Content-Type': 'application/json; charset=UTF-8'
  }

  # 请求返回
  res = requests.get(url, headers=headers)

  # 检查返回状态
  if res.json()['status'] or res.json()['status'] == 0:
    return res.json()
  else:
    return {'status': '211', 'msg': '请求错误'}
