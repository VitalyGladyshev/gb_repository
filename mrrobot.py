# coding: utf-8

# Python. Быстрый старт.
# Занятие 8.

# Домашнее задание: 
#       в модуле робота создать функцию удаления случайного файла из указанной директории;
#       при проигрыше сделать случайный выбор наказания - либо дублирование файлов, либо удаление файла.


import os
import sys
import shutil
import random
import psutil


def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)  # копируй
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
            return True
        else:
            print("Возникли проблемы копирования")
            return False


def duble_files(dirname):
    file_list = os.listdir(dirname)
    i = 0
    while i < len(file_list):
        # Не забываем сформировать полный путь к файлу
        fullname = os.path.join(dirname, file_list[i])
        duplicate_file(fullname)
        i += 1


def sys_info():
    print("Вот что я знаю о системе:")
    print("Количество процессоров: ", psutil.cpu_count())
    print("Платформа: ", sys.platform)
    print("Кодировка файловой системы: ", sys.getfilesystemencoding())
    print("Текущая директория: ", os.getcwd())
    print("Текущий пользователь: ", os.getlogin())


def del_dublicats(dirname):
    file_list = os.listdir(dirname)
    doubl_count = 0
    for f in file_list:
        fullname = os.path.join(dirname, f)  # \ /
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                print("Файл ", fullname, " был удален")
                doubl_count += 1
    return doubl_count


def random_delete(dirname):
    file_list = os.listdir(dirname)
    file_count = 0
    for i in file_list:
        fullname = os.path.join(dirname, i)
        if os.path.isfile(fullname):
            file_count += 1
    lucky_file = random.randint(1, file_count)
    file_count = 0
    for i in file_list:
        fullname = os.path.join(dirname, i)
        if os.path.isfile(fullname):
            file_count += 1
            if file_count == lucky_file:
                os.remove(fullname)
                print("Файл ", fullname, " был удален")


# Комментарий

def main():
    print("Great Python Program!")
    print("Привет, программист!")
    name = input("Ваше имя: ")

    print(name, ", добро пожаловать в мир Python!")

    answer = ''
    # PEP-8    
    while answer != 'q':
        answer = input("Давайте поработаем? (Y/N/q)")
        if answer == 'Y':
            print("Отлично, хозяин!")
            print("Я умею:")
            print(" [1] - выведу список файлов")
            print(" [2] - выведу информацию о системе")
            print(" [3] - выведу список процессов")
            print(" [4] - продублирую файлы в текущей директории")
            print(" [5] - продублирую указанный файл")
            print(" [6] - удалю дубликаты файлов")
            print(" [7] - удалю случайный файл :)")
            do = int(input("Укажите номер действия: "))

            if do == 1:
                print(os.listdir())

            elif do == 2:
                sys_info()

            elif do == 3:
                print(psutil.pids())

            elif do == 4:
                print("=Дублирование файлов в текущей директории=")
                duble_files('.')

            elif do == 5:
                print("=Дублирование указанного файла=")
                filename = input("Укажите имя файла:")
                duplicate_file(filename)

            elif do == 6:
                print("=Удаление дубликатов в директории=")
                dirname = input("Укажите имя директории:")
                count = del_dublicats(dirname)
                print("-- Удалено файлов: ", count)

            elif do == 7:
                print("=Удаление случайного файла=")
                dirname = input("Укажите имя директории:")
                random_delete(dirname)

            else:
                pass

        elif answer == 'N':
            print("До свидания!")
        else:
            print("Неизвестный ответ")

print("Новый парметр")


if __name__ == "__main__":
    main()
