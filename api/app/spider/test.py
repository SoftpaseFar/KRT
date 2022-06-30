# from flask import Flask, session
# import os
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = os.urandom(24)




















# import requests
#
# # "031wY7ll2tODq947D8nl2lyXiX3wY7lE"
# code = '0915iy1w3qLpMY2WIS3w3wkeyD25iy1Z'
# url = 'https://api.weixin.qq.com/sns/jscode2session?appid=wxce6a5c19d66a83de&secret=44e2995af4111ab719975ba7b2a36c7c&js_code=' + code + '&grant_type=authorization_code'
#
# res = requests.get(url)
# print(res.json())
#
# res_code = {
#   'session_key': '+TUCfA9iLkSFQbnQSa5Beg==',
#   'expires_in': 7200,
#   'openid': 'oBjvt0OP4c3rmNno-iu8xPhBR8ME'
# }
#
#
#
# import random
#
# def get_rand_chars(length):
#   str = ""
#   str_pol = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm"
#   max_num = len(str_pol)
#   for i in range(0, length):
#     str += str_pol[random.randint(0, max_num-1)]
#   return str
#
#
# print(get_rand_chars(32))
# import time
#
# time_stamp = time.time()
# print(time_stamp)


