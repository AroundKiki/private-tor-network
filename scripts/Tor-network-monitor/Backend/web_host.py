# 运行于主机当中，监听请求


from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/tor-monitor/resize', methods=['POST'])
def resize():
    print(request.form)
    r = requests.get('https://127.0.0.1:5000/tor-monitor/init',)
    # TODO: 将表单转换为命令

    return [r.status_code, r.text]
    # post数量


def command():
    # 启动攻击等
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
