import socket
import threading
import time
def clit(address_):
    tcp_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #建立连接
    tcp_sock.connect(address_)
    #发送数据
    data=f"{time.ctime()} hello"
    tcp_sock.send(data.encode())
    #关闭连接
    tcp_sock.close()
if __name__ == '__main__':
    address=("127.0.0.1",7000)
    task=[]
    for i in range(100):
        t=threading.Thread(target=clit, args=(address,))
        task.append(t)
        t.start()
    for t in task:
        t.join()