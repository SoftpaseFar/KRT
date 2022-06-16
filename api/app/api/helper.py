from flask import jsonify, request
from . import api
from app.forms.weather import WeatherForm
from app.spider.weather import get_weather


@api.route("/v1/helper/weather", methods=['POST'])
def get_weather_info():
  # 验证参数
  form = WeatherForm(request.args)
  if form.validate():
    res = get_weather(form.latitude.data, form.longitude.data)
    return jsonify(res)
  else:
    return jsonify({
      'status':'211',
      'msg':form.errors
    })
