from flask import jsonify, request
from app.api import api
from app.forms.book import SearchForm
import time


@api.route("/v1/hello")
def get_one_json():
  form = SearchForm(request.args)
  if form.validate():
    x = form.x.data
    y = form.y.data
    res = {"hello": x, "number": y}
    return jsonify(res)
  else:
    return jsonify(form.errors)


@api.route("/v1/test")
def test():
  # pass

  return jsonify({
    "date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    "author": "SapereAude",
    "age": 22,
    "country": "China"
  })


