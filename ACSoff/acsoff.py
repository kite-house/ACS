# SERVER

import socket
import sys



def server():
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(99)
    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            continue

        if data:
            if data == b'test':
                conn.send('completed'.encode())

            if data == b'closed change':
                conn.send('x.report completed'.encode())
                wait_com = conn.recv(1024)
                if wait_com == b'permission completed':
                    # выполняем функцию
                    conn.send("closed change completed".encode())
                    sys.exit()

if __name__ == '__main__':
    try:
        server()
    except Exception as error:
        print(f'ERROR: {error}')