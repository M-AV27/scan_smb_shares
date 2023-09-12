import socket
import os

from config import login, password, list_ipaddress, current_date_time
from re_func import re_pc_name, re_pars_shares
from pars_dir import parse_direcory
from socket_ip_name import get_host_name
from tqdm import tqdm 


file = open(os.path.join('results', f'{current_date_time}.txt'), 'a', encoding='utf-8')   # Создаем файл с именем текущей даты_времени в папке results
def main():
    for ip in tqdm(list_ipaddress): 	# Идем по ip адресам в списке
    
        host_name = get_host_name(str(ip)) 	# Получаем имя хоста
    
        if host_name and re_pc_name(host_name, check_name=True):  #Проверяем на соответсвие, при положительном результате записывеам результат в файл
            host_name = re_pc_name(host_name, find_name=True)[0]
            result = parse_direcory(login, password, host_name)
            if re_pars_shares(result):
                result = re_pars_shares(result)
                file.writelines(f'{host_name} ({ip}) ')
                file.writelines([i + ' ' for i in result])
                file.writelines('\n')
            else:
                continue
        else:
            continue

file.close()

if __name__ ==  '__main__':
    main()



