"""
Controller类的实例中维护着所有tor节点的stem控制器
提供两个方法返回信息
"""

import stem
import stem.connection
from stem.control import EventType


class Controller(object):
    ROLE_LIST = ['da', 'relay', 'exit', 'client']

    def __init__(self, node_list):
        """

        :param node_list: node_list[role_name] = list[node_name, node_ip]
        初始化实例，生成所有Tor节点的控制器
        """
        print('MSG: Initializing Tor controller')
        self.controller_list = {}
        self.speed_list = {}
        self.conf_list = {}
        for role in self.ROLE_LIST:             #初始化
            self.controller_list[role] = []
        for role in self.ROLE_LIST:
            role_list = node_list[role]  #某一角色的所有node列表
            for node in role_list:      #node [ip,主机名]
                node_name = node[1]
                node_controller = stem.connection.connect(
                    control_port=(str(node[0]), 'default'),
                    password="password")
                if node_controller is None:
                    print("create controller error")
                    exit(1)
                node_controller.add_event_listener(self.bw_handler, EventType.BW)
                self.controller_list[role].append([node_name, node_controller])
            print('MSG: Init complete')

    def get_speed(self):
        # 所有结点的带宽信息
        self.speed_list = {'code': 20000, 'data': []} #code为返回前端的状态码
        for role in self.ROLE_LIST:
            role_list = self.controller_list[role]
            for node in role_list:
                cache = node[1].get_info('bw-event-cache', None)
                last_speed = cache.split()
                node_info = {'name': node[0], 'speed_str': last_speed[-60:]}
                print(node_info)
                self.speed_list['data'].append(node_info)
        return self.speed_list
                # print('%s, download speed(B/s): %s, upload speed(B/s): %s' % (node[0], last_speed[-1].split(',')[0], last_speed[-1].split(',')[1]))

                # print(node[0])
                # print(node[1].get_info('bw-event-cache', None))

    def get_conf(self):
        # 获得所有主机配置文件
        self.conf_list = {'code': 20000, 'data': []}
        for role in self.ROLE_LIST:
            role_list = self.controller_list[role]
            for node in role_list:
                cache = node[1].get_info('config-text', None)
                conf = cache.splitlines()
                conf_dict = {}
                for attr in conf:
                    if ' ' not in attr:
                        continue
                    temp = attr.split(' ', 1)
                    conf_dict[temp[0]] = temp[1]
                node_info = {'name': node[0], 'conf': conf_dict}
                print(node_info)
                self.conf_list['data'].append(node_info)
        return self.conf_list

    def bw_handler(self, event):
        # cannot remove!!!
        # 空回调函数用于不断刷新bw-enent-cache
        pass




