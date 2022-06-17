import requests
from lxml import etree
from app.libs.httper import get_word_from_url


def certificate(stu_verif_code):
  host = 'https://www.chsi.com.cn'
  html_text = requests.get(host + '/xlcx/bg.do?vcode=%s' % str(stu_verif_code))
  res = etree.HTML(html_text.text)

  name_and_graduation_url = res.xpath('//div[@class="div2"]//tr//td//img[@class="by_img"]/@src')
  try:
    name_url = host + name_and_graduation_url[0]
    is_graduation_url = host + name_and_graduation_url[1]
    name = get_word_from_url(name_url)['prism_wordsInfo'][0]['word']
    is_graduation = get_word_from_url(is_graduation_url)['prism_wordsInfo'][0]['word']
  except IndexError:
    return {
      'status': '210',
      'msg': '请求错误'
    }

  stu_info = res.xpath('//div[@class="div2"]//tr//td/span//text()')

  try:
    sex = stu_info[0] if stu_info[0] else "未知"
    date_of_birth = stu_info[1] if stu_info[1] else "未知"
    admission_date = stu_info[2] if stu_info[2] else "未知"
    graduation_date = stu_info[3] if stu_info[3] else "未知"
    edu_category = stu_info[4] if stu_info[4] else "未知"
    edu_level = stu_info[5] if stu_info[5] else "未知"
    school_name = stu_info[6] if stu_info[6] else "未知"
    academic_system = stu_info[7] if stu_info[7] else "未知"
    major = stu_info[8] if stu_info[8] else "未知"
    ways_of_learning = stu_info[9] if stu_info[9] else "未知"
    certificate_no = stu_info[10] if stu_info[10] else "未知"
    headmaster = stu_info[11] if stu_info[11] else "未知"
    res = {
      'name': name,
      'sex': sex,
      'date_of_birth': date_of_birth,
      'admission_date': admission_date,
      'graduation_date': graduation_date,
      'edu_category': edu_category,
      'edu_level': edu_level,
      'school_name': school_name,
      'academic_system': academic_system,
      'major': major,
      'ways_of_learning': ways_of_learning,
      'certificate_no': certificate_no,
      'is_graduation': is_graduation,
      'headmaster': headmaster
    }

    return {
      'status': '205',
      'msg': '获取成功',
      'data': res
    }
  except IndexError:
    return {
      'status': '210',
      'msg': '请求错误'
    }
