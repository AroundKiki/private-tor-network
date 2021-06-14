# 运行于Docker容器当中，监听web请求


import socket
from datetime import datetime
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/tor-monitor/info', methods=['GET'])
def info():
    data = "INFO"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect(('127.0.0.1', 9999))
        # sock.connect("./tmp/test.sock")
        print("client {0} 发送 {1}".format(datetime.now(), data))
        sock.sendall(bytes(data, "utf-8"))
        received_data = sock.recv(81920)
        print("client {0} 收到 {1}".format(datetime.now(), received_data))

    return received_data


@app.route('/tor-monitor/bw', methods=['GET'])
def bw():
    data = "BW"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect(('127.0.0.1', 9999))
        # sock.connect("./tmp/test.sock")
        print("client {0} 发送 {1}".format(datetime.now(),data))
        sock.sendall(bytes(data,"utf-8"))
        received_data = sock.recv(81920)
        print("client {0} 收到 {1}".format(datetime.now(),received_data))

    return received_data


@app.route('/tor-monitor/init', methods=['GET'])
def init():
    data = "INIT"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect(('127.0.0.1', 9999))
        # sock.connect("./tmp/test.sock")
        print("client {0} 发送 {1}".format(datetime.now(), data))
        sock.sendall(bytes(data, "utf-8"))
        received_data = sock.recv(81920)
        print("client {0} 收到 {1}".format(datetime.now(), received_data))

    return received_data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




# if __name__ == "__main__":
#     data = "test string"
#     with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
#         # sock.connect("./tmp/test.sock")
#         sock.connect(('127.0.0.1', 9999))
#
#         print("client {0} 发送 {1}".format(datetime.now(),data))
#         sock.sendall(bytes(data,"utf-8"))
#
#         received_data = sock.recv(4096)
#         print("client {0} 收到 {1}".format(datetime.now(),received_data))
