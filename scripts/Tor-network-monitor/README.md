# Tor-network-monitor
## 运行

在Docker启动后，某一容器内（例如client容器）
切换到工作目录
```python
nohup python3 main.py &
nohup python3 Backend/client.py &
```

在宿主机当中运行
```python
nohup python3 Backend/host.py &
```



