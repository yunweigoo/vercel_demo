from flask import Flask, jsonify, request
from vercel.wsgi import VercelWSGI

app = Flask(__name__)

@app.route('/api')
def hello():
    return jsonify({"message": "Hello from Flask on Vercel!"})

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.get_json()
    # 在这里处理POST请求的数据
    return jsonify({"received": data})

# 重点：使用 VercelWSGI 适配器
app_wsgi = VercelWSGI(app)

def main(request):
    return app_wsgi(request)