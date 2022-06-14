from flask import jsonify
from . import web


@web.route("/search/<book>/<number>")
def search(book, number):
  headers = {
    'content-type': 'application/json',
    # 'location': 'https://www.bing.com'
  }
  return '{"book":"%s","number":"%s"}' % (book, number), 201, headers


@web.route("/search/book")
def get_one_json():
  res = {"book": "521", "number": "521"}
  # return json.dumps(res), 200, {"content-type": "application/json"}
  return jsonify(res)

# app.add_url_rule("/", view_func=hello)
