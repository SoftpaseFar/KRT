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


# 阿里短信
def ali_api_request(mobile, param):
  res_url = 'https://gyytz.market.alicloudapi.com/sms/smsSend'

  headers = {
    'Authorization': 'APPCODE ' + current_app.config["ALI_SMS_URL_APPCODE"],
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
  }

  data = {
    'mobile': mobile,
    'param': param,  # '**code**:12345,**minute**:5'
    'smsSignId': current_app.config["ALI_SMSSIGNID"],
    'templateId': current_app.config["ALI_TEMPLATEID"]
  }

  data = json.dumps(data)

  res = requests.post(url=res_url, headers=headers, data=data)
  return res.json()
