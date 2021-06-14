import socket

relay_num = 0
exit_num = 0

# relay_list = socket.getaddrinfo("relay",0,type=2)
# relay_num = len(relay_list)
#
# relay_ip = []       #[ip, 主机名]
# for m in relay_list:
#     relay_ip.append([m[4][0], ""])
# for i in range(len(relay_ip)):
#     relay_ip[i][1] = socket.gethostbyaddr(relay_ip[i][0])[0]


def get_role(role_name):                #获得对应角色的ip和主机名
    role_info_raw = socket.getaddrinfo(role_name, 0, type=2)
    role_list = []          # [ip, 主机名]
    for m in role_info_raw:
        role_list.append([m[4][0], ""])
    for i in range(len(role_list)):
        role_list[i][1] = socket.gethostbyaddr(role_list[i][0])[0]
    return role_list


if __name__== "__main__":
    relay_list = get_role("relay")
    exit_list = get_role("exit")
    client_list = get_role("client")
    print(relay_list, exit_list, client_list)


