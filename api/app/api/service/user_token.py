import hashlib
import random
import time
import datetime
from flask import current_app, session
import requests
import json
from app import db
from app.models.user import User


# 设置缓存时间 分钟
def session_setting(seconds):
  session.permanent = True
  current_app.permanent_session_lifetime = datetime.timedelta(seconds=seconds)


# 写入缓存
def session_write(key, value, seconds):
  session_setting(seconds)
  session[key] = value


# 获取wx_result
def user_wx_result_get(code):
  url = "https://api.weixin.qq.com/sns/jscode2session?appid=" + \
        current_app.config["WX_APPID"] + "&secret=" + \
        current_app.config["WX_SECRET"] + "&js_code=" + \
        code + "&grant_type=authorization_code"

  res = requests.get(url)

  return res


# 获取随机字符串
def get_rand_chars(length):
  str = ""
  str_pol = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm"
  max_num = len(str_pol)
  for i in range(0, length):
    str += str_pol[random.randint(0, max_num - 1)]
  return str


# token生成
def generate_token():
  # 32个字符组成一组随机字符串
  rand_chars = get_rand_chars(32)
  # 获取访问的时间戳
  time_stamp = time.time()
  # salt盐
  salt = current_app.config["TOKEN_SALT"]
  # md5加密
  token = hashlib.md5((rand_chars + str(time_stamp) + salt).encode(encoding='UTF-8')).hexdigest()
  return token


#  颁发令牌
def grantToken(wx_result):
  #  1.拿到openID
  open_id = wx_result['openid']
  # 返回格式示例
  #  {
  #   'session_key': '+TUCf666LkSFQbnQSa5Beg==',
  #   'expires_in': 7200,
  #   'openid': 'oBjv886P4c3rmNno-iu8xPhBR8ME'
  # }
  # 2.数据库里看一下是否已经存在
  user = User.query.filter_by(wx_open_id=open_id).first()
  if user:
    uid = user.id
  else:
    new_user = User()
    new_user.wx_open_id = open_id
    new_user.nickname = "test"
    new_user.password = "123456"
    new_user.creat_time = datetime.datetime.now()
    db.session.add(new_user)
    db.session.commit()
    uid = new_user.id
  # 如果存在则不处理，不存在则新增一条user数据
  # 3.生成令牌，准备缓存，写入缓存
  # key: 令牌
  # value:wxResult uid scope权限
  cache_value = {
    "uid": uid,
    "wx_result": wx_result,
    "scope": 16
  }

  cache_value = json.dumps(cache_value)
  # 获取token
  key = generate_token()
  # 缓存时长
  expire_in = current_app.config["TOKEN_EXPIRE_IN"]
  # 写入缓存
  session_write(key, cache_value, expire_in)

  # 把令牌返回到客户端去
  return key


# 获取token
def user_token_get(code):
  wx_result = user_wx_result_get(code).json()
  if 'errcode' in wx_result:
    return {
      "status": wx_result['errcode'],
      "msg": wx_result['errmsg']
    }
  else:
    token = grantToken(wx_result)
    return {
      "status": "200",
      "msg": "获取成功",
      "token": token
    }


def get_current_token_var(token, key):
  var_s = session.get(token)
  if not var_s:
    raise Exception("token不存在或者失效")
  else:
    var_s = json.loads(var_s)
    return var_s[key]


# 根据token获取当前用户的uid
def get_current_uid(token):
  uid = get_current_token_var(token, "uid")
  print(uid)
