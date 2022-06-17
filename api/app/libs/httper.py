import json
import requests
from flask import current_app


# 阿里图片文字提取
def get_word_from_url(url):
  headers = {
    'Authorization': 'APPCODE ' + current_app.config["ALI_STU_URL_APPCODE"],
    'Content-Type': 'application/json; charset=utf-8'
  }

  data = {
    'url': url
  }
  data = json.dumps(data)

  request_url = "https://lysbwdxs.market.alicloudapi.com/ocrservice/document"

  res = requests.post(url=request_url, headers=headers, data=data)
  return res.json()
