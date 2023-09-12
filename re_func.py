import re


# Функция проверки корректности имени или поиска имени ПК в строке
# Флаг find_name = True для поиска имени
# Флаг check_name = True для проверки
def re_pc_name(name, find_name=False, check_name=False):

    pattern_re = r'' #Добавить свой шаблон re тут


    if re.match(pattern_re, name) and check_name:
        return True


    if find_name:                  # Поиск имени ПК в строке
        return re.findall(pattern_re, name)
    else:
        return False


#Функция отсеивания системных директорий C$, ADMIN$ и т.п
def re_pars_shares(list_shares):

    result_list = []
    pattern_re = r'\b\w*\$\B'

    for i in list_shares:
        if re.findall(pattern_re, i):
            continue
        else:
            result_list.append(i)

    return result_list