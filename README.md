## 使用方法:

```
# 编译镜像（仅需一次）
docker build -t cc/private-tor .

#启动docker集群
docker-compose up -d

#启动主机端管理程序
nohup python3 scripts/Tor-network-monitor/Backend/web_host.py &
```

## 调节节点数量
使用docker exec进入各主机内部环境
client节点具有socks5代理

da、relay、exit可以使用--scale标签调节数量

```
docker-compose up -d  --scale da=4 --scale exit=3
```

client节点需要在docker-compose.yml文件中，取消固定的端口映射后，才可以使用--scale调节数量

hs节点的代理目标docker-compose.yml文件中定义，scale标签生成的多个hs会指向同一个被代理节点

## 网络节点
具有relay，exit，hs（隐藏服务），client（Tor用户客户端）节点，backend管理后端容器，web、ftp、ddos等功能性容器。


## 目录结构
script文件夹中的Tor-network-monitor为管理后端程序，script文件夹中的文件会在容器启动时自动拷贝到容器当中
