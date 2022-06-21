from app.libs.httper import ali_api_request


def sms_ver_service(mobile, code):
  param = '**code**:' + code + ',**minute**:5'
  res = ali_api_request(mobile, param)
  # TODO session部分
  return res
