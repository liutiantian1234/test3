import socket
import time
import threading
lock = threading.Lock()
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址与端口
address = ("0.0.0.0", 7000)
def comput(cnct, addr):
    # 接收数据
    data = cnct.recv(1024)
    print(f"接收到{addr}的数据:{data}")
     # 断开连接
    cnct_.close()


if __name__ == '__main__':
    task = []
# 新建一个TCP_socket
    tcp_sock.bind(address)
    print(f"bind {address}...")
# 监听
    tcp_sock.listen(10)
    print("linsting...")
    while True:
        cnct_, addr_ = tcp_sock.accept()
        t = threading.Thread(target=comput, args=(cnct_, addr_,))
        task.append(t)
        t.start()
        for t in task:
            t.join()
       