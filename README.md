## ʹ�÷���:

```
# ���뾵�񣨽���һ�Σ�
docker build -t cc/private-tor .

#����docker��Ⱥ
docker-compose up -d

#���������˹������
nohup python3 scripts/Tor-network-monitor/Backend/web_host.py &
```

## ���ڽڵ�����
ʹ��docker exec����������ڲ�����
client�ڵ����socks5����

da��relay��exit����ʹ��--scale��ǩ��������

```
docker-compose up -d  --scale da=4 --scale exit=3
```

client�ڵ���Ҫ��docker-compose.yml�ļ��У�ȡ���̶��Ķ˿�ӳ��󣬲ſ���ʹ��--scale��������

hs�ڵ�Ĵ���Ŀ��docker-compose.yml�ļ��ж��壬scale��ǩ���ɵĶ��hs��ָ��ͬһ��������ڵ�

## ����ڵ�
����relay��exit��hs�����ط��񣩣�client��Tor�û��ͻ��ˣ��ڵ㣬backend������������web��ftp��ddos�ȹ�����������


## Ŀ¼�ṹ
script�ļ����е�Tor-network-monitorΪ�����˳���script�ļ����е��ļ�������������ʱ�Զ���������������
