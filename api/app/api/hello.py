from flask import jsonify, request
from . import api
from ..forms.book import SearchForm


@api.route("/hello")
def get_one_json():
  form = SearchForm(request.args)
  if form.validate():
    x = form.x.data
    y = form.y.data
    res = {"hello": x, "number": y}
    return jsonify(res)
  else:
    return jsonify(form.errors)
