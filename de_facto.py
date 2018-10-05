#!/usr/bin/python3
#Программа написана Alexander Bigulov 05.10.2018. Версия 1.0 release
def openfile (file, atr):  #Открываем файлик
    handle = open(file, atr)
    data = handle.readlines()
    handle.close()
    return data
def is_photoshop(file):  #Был ли файл изменён фотошопом?
    data = openfile(file, 'rb')  #Читаем файл
    isPhotoshop = False  #Переменная для позднейшей проверки
    for string in data:  #Перебираем массив картинки
        if "Photoshop".encode('utf-8') in string: #Смотрим, содержит ли фотощоп
            print('Хех. Это фото было изменено Adobe Photoshop.')
            print("Доказательство:")
            print(str(string))
            isPhotoshop = True  #Говорим, что было изменено
            break  #Кончаем цикл! Одного пруфа хватит!
    if isPhotoshop == False:  #Та самая проверка на неизменённость
        print('Этот файл не был изменён Adobe Photoshop.')
filename = input('Имя файла: ')
is_photoshop(filename)  #Собсна всё