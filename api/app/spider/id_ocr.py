from datetime import datetime as pydatetime
from flask import current_app
import hmac, hashlib
import requests
import base64


def ver_id_info(front, negative):


  # 请求url
  url = 'https://service-7q4laj51-1307960160.sh.apigw.tencentcs.com/release/ocr/idcard'

  # 验证信息
  secretId = current_app.config["T_SECRETID"]
  secretKey = current_app.config["T_SECRETKEY"]

  data = {
    "front": front,
    "negative": negative
  }
  source = "market"

  # 签名
  datetime = pydatetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
  signStr = "x-date: %s\nx-source: %s" % (datetime, source)
  sign = base64.b64encode(hmac.new(secretKey.encode('utf-8'), signStr.encode('utf-8'), hashlib.sha1).digest())
  auth = 'hmac id="%s", algorithm="hmac-sha1", headers="x-date x-source", signature="%s"' % (
    secretId, sign.decode('utf-8'))


  headers = {
    'X-Source': source,
    'X-Date': datetime,
    'Authorization': auth,
  }

  r = requests.post(url, headers=headers, data=data)
  return r.json()
