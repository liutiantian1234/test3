import socket
global i,j,k
i=0
j=0
k=0
list1={}
tcp_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address=('0.0.0.0',7000)
tcp_sock.bind(address)
tcp_sock.listen(10)
while True:
    com,addr=tcp_sock.accept()
    i=i+1
    print(f"连接了{i}次")
    data=com.recv(1024)
    print(f"接收的数据：{data}")
    list1[i]=data
    print(list1)
    com.send(data)
    j=len(data)
    k=k+j
    print(f"总共接收了{k}字节") 
    data2=f"数据：{data}，连接次数：{i}"
    com.send(data2.encode())
    com.close()

