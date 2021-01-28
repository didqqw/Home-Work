import socket
import time
import threading


key = 8194

shutdown = False
join = False

# Функция, которая будет обробатывать все наши данные
def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(2048)
                # print(data.decode("utf-8"))

                # Начало
                decrypt = ""; k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i)^key)
                print(decrypt)
                # Конец

                time.sleep(0.1)
        except:
            pass

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.1.243", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

alias = input("Введите свой ник: ")
print("""


░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝

        """)

rT = threading.Thread(target = receving, args = ("RecvThread", s))
rT.start()

while shutdown == False:
    if join == False:
        s.sendto(("\n["+ alias +"] - вошел(-ла) в чат ").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input("\nВведите сообщение: ")

            crypt = ""
            for i in message:
                crypt += chr(ord(i)^key)
            message = crypt

            if message != "":
                s.sendto(("\n["+ alias +"] :: " + message).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            s.sendto(("\n["+ alias +"] - вышел из чата ").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()