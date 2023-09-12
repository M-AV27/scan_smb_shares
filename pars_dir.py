import socket
import smb
from smb.SMBConnection import SMBConnection
from config import domain

# Функция получения данных SMB протокола хоста
def parse_direcory(login, password, remote_name):

    connection = SMBConnection(username=login, password=password, my_name='login', \
                         remote_name=remote_name, domain=domain)
    list_find_shares = []

    try:
        connection.connect(remote_name, 139)
        for i in connection.listShares():
            list_find_shares.append(i.name)
    except smb.base.NotReadyError:
        return ('smb Проблема авторизации SMB')
    except smb.base.NotConnectedError:
        return ('smb Проблема соединения')
    except TimeoutError:
        return ('System Timeout')
    except smb.base.SMBTimeout:
        return ('SMBTimeout')
    except socket.gaierror:
        return ('socket Проблема авторизации')

    connection.close()

    return list_find_shares
