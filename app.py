from flask import Flask
from api import api  # 导入 api 蓝图模块

app = Flask(__name__)

# 注册 API 蓝图
app.register_blueprint(api, url_prefix='/api')

# 首页路由
@app.route('/')
def hello_world():
    return 'Hello, Vercel Flask!'

if __name__ == '__main__':
    app.run()
