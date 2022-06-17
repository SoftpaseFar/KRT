from flask import jsonify, request
from . import api
from app.forms.weather import WeatherForm
from app.spider.weather import get_weather
from app.forms.id_ocr import IdInfoForm
from app.spider.id_ocr import ver_id_info
from app.forms.stu_ver import StuVerForm
from app.spider.stu_cer import certificate


# 根据经纬度获取7天天气
@api.route("/v1/helper/weather", methods=['POST'])
def get_weather_info():
  # 验证参数
  form = WeatherForm(request.args)
  # 返回数据
  if form.validate():
    res = get_weather(form.latitude.data, form.longitude.data)
    return jsonify(res)
  else:
    return jsonify({
      'status': '211',
      'msg': form.errors
    })


# 身份证正反面信息提取
@api.route("/v1/helper/id_info", methods=['POST'])
def get_info_from_id():
  form = IdInfoForm(request.args)
  if form.validate():
    res = ver_id_info(form.front.data, form.negative.data)
    res["status"] = res.pop("code")
    print(res)
    return jsonify(res)
  else:
    return jsonify({
      'status': '211',
      'msg': form.errors
    })


# 学生信息认证
@api.route("/v1/helper/student_info", methods=['POST'])
def get_info_from_student_code():
  form = StuVerForm(request.args)
  if form.validate():
    res = certificate(form.verif_code.data)
    return jsonify(res)
  else:
    return jsonify({
      'status': '211',
      'msg': form.errors
    })



# 短信验证码
# https://market.cloud.tencent.com/products/32818
# verif_code = 'AUBGKX3N00G7H3BC'
