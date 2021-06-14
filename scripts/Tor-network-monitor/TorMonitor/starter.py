import TorMonitor.get_info as get_info
from TorMonitor.controller import Controller
import time
from threading import Thread
import socket
import json

ROLE_LIST = ['da', 'relay', 'exit', 'client']
ctr = None


def bw_loop():
    # 程序主循环，socket和Backend/web_docker.py通讯
    global ctr
    # while True:
    #     for role in ROLE_LIST:
    #         # ctr.get_speed(role)
    #         print('1')
    #     time.sleep(1)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_sock:
        s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s_sock:
        # if os.path.exists("/tmp/test.sock"):
        #     os.unlink("/tmp/test.sock")
        s_host = ('127.0.0.1', 9999)
        s_sock.bind(s_host)  # 第一步：bind
        # s_sock.bind("./tmp/test.sock") # 第一步：bind
        s_sock.listen(5)  # 第二步：listen
        print("服务端启动完成")
        while True:
            c_sock, c_addr = s_sock.accept()  # 第三步：接收客户端连接
            print("收到来自 {0} 的连接请求".format(c_addr))
            c_data = c_sock.recv(4096)  # 读取客户端发来的数据
            c_str = str(c_data, "utf-8")  # 由字节序列转码成utf-8字符串
            print("收到来自 {0} 的信息 '{1}' ".format(c_addr, c_str))

            if c_str == 'BW':
                c_sock.sendall(bytes(bw_handler(), "utf-8"))  # 发送带宽信息，即前端bw_raw
            elif c_str == 'INFO':
                c_sock.sendall(bytes(info_handler(), "utf-8"))  # 发送节点信息
            elif c_str == 'INIT':
                c_sock.sendall(bytes(init_handler(), "utf-8"))



def main():
    # 程序入口
    role_list = {}
    for role in ROLE_LIST:
        print("MSG: Getting %s List" % role)
        role_list[role] = get_info.get_role(role)
        for node in role_list[role]:
            print('MSG: Node IP: %s, Hostname: %s' % (node[0], node[1]))

    global ctr
    ctr = Controller(role_list)
    bw_loop()
    # thread1 = Thread(target=bw_loop)
    # thread2 = Thread(target=server)


def bw_handler():
    # 网络流量数据json化
    global ctr
    speed = ctr.get_speed()
    print(speed)
    return json.dumps(speed)


def info_handler():
    # 配置文件数据json化
    global ctr
    config = ctr.get_conf()
    print(config)
    return json.dumps(config)


def init_handler():
    # 网络节点数量有变化时，重置Controller类的实例ctr
    role_list = {}
    for role in ROLE_LIST:
        print("MSG: Getting %s List" % role)
        role_list[role] = get_info.get_role(role)
        for node in role_list[role]:
            print('MSG: Node IP: %s, Hostname: %s' % (node[0], node[1]))

    global ctr
    ctr = Controller(role_list)
    print('init_handler finish')
    print(ctr.controller_list)
    return "init ok"
