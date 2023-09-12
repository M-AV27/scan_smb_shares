import socket

# Функция получения имени хоста из ip
def get_host_name(ip):

    socket_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_connect.settimeout(0.02)
    connect = socket_connect.connect_ex((ip, 139))

    if connect == 0:
        try:
            host_name = str(socket.gethostbyaddr(str(ip))[0])
            return host_name
        except socket.herror:
            return False # 'Не удалось получить имя хоста'




