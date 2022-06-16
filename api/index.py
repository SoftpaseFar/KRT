from app import create_app
from flask import jsonify

app = create_app()

@app.errorhandler(Exception)
def error_handler(e):
    data = {
        "status": -1,
        "err": str(e),
        "msg": "调用错误"
    }
    return jsonify(data)

if __name__ == '__main__':
  # 生产环境 nginx + uwsgi
  app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=80)
