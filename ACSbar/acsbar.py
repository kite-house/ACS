# CLIENT

import socket
import sys
# start

sock = socket.socket()

def check_connection():
    sock.connect(('localhost', 9090))
    sock.send('test'.encode())
    data = sock.recv(1024)
    return data

def send_command():
    command = 'closed change'.encode()
    sock.send(command)

print("--ACS SYSTEM--")
confirmation = 'None'
password = str(input("Input password: "))
if password == 'helloworld':
    print("ACCESS COMPLETED")
    print('Проверяем подключение...')
    if check_connection() == b'completed':
        print('Успешно! Подключение установлено.')
        while confirmation != 'y' and confirmation != 'n':
            confirmation = str(input('Вы уверены что хотите закрыть смену(Это действия нельзя отменить)?(y/n): '))

        if confirmation == 'y':
            print("Команда закрыть смену, отправлена")
            send_command()
            wait_x_report = sock.recv(1024)
            if wait_x_report == b'x.report completed':
                print("x.отчёт выполнен, отправляем протокол с разрешением закрытие смены...")
                sock.send('permission completed'.encode())
                # Выполняем функции
                finish = sock.recv(1024)
                if finish == b'closed change completed':
                    print("Обе системы закрыли смены.")
                    sys.exit()

        
        elif confirmation == 'n':
            print("Хорошо отмена")

    else: 
        print('Ошибка! Подключение не установлено!')


else: print('ACCESS BANNED')