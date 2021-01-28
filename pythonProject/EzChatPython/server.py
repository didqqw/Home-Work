import socket
import time

# Переменные IP-адреса, можно так же использовать ""свой IP""

host = socket.gethostbyname(socket.gethostname())
# Порт сервера, можно взять любой, если вы уверены, что он свободный
port = 9090

clients = []  # Пустой список клиентов

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Переменная протокола TCP/IP
s.bind((host, port))  # Объявляем на создание HOST name и PORT

quit = False  # Переменная нужна, чтобы можно было остановить цикл
print("[ Статус сервера: Включен ]")  # Вывод в консоли при запуске сервера

while not quit:
    try:
        # data - переменная для пакетов сообщений, addr - личный адрес пользователя
        # s.recv from 1024 размер данных которые можно отправить
        data, addr = s.recvfrom(2048)

        if addr not in clients:
            clients.append(addr)

        # Формат в котором будут отоброжаться сообщения в консоли
        p = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + p + "]/", end="")
        print(data.decode("utf-8"))  # Вариант шифрования, декодирование на сервере

        for client in clients:  # Что бы клиенту не отпровлялись свои же сообщения
            if addr != client:
                s.sendto(data, client)

    except:
        print("\n[ Статус сервера: Отключен ]")
        quit = True

s.close()
