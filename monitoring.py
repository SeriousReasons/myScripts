#---------------------------
#                           
# Script by Serious.Reasons 
#                           
#---------------------------

import requests, logging
from sys import argv
from time import sleep
from prettytable import PrettyTable
from colorama import Fore

#Переменная для хранения времени задержки
sleepTime = int(argv[1])

#Удаление лишних параметров
del argv[0:2]

#Создание таблицы
monitorTable = PrettyTable()
#Наименование столбцов таблицы
monitorTable.field_names = ["URL", "Time delay, sec", "Response code", "Status"]

#Основной цикл мониторинга
while True:

    #Время задержки между запросами
    sleep(sleepTime)
    #Отчистка строк таблицы                                                 
    monitorTable.clear_rows()

    #Цикл отпраки GET-запросов на URL
    for i in range(len(argv)):

        #Отправка GET-запроса
        response = requests.get(argv[i])

        #Переменная для хранения статуса URL
        status = ""

        #Определение типа полученного кода ответа
        match response.status_code:
            case code if 100 <= code <= 199:
                status = Fore.WHITE + "Informational code" + Fore.RESET
            case 200:
                status = Fore.GREEN + "OK" + Fore.RESET
            case code if 201 <= code <= 299:
                status = Fore.GREEN + "Success code" + Fore.RESET
            case code if 300 <= code <= 399:
                status = Fore.YELLOW + "Redirection" + Fore.RESET
            case 404:
                status = Fore.RED + "Not Found" + Fore.RESET
            case code if 400 <= code <= 499:
                status = Fore.RED + "Client error" + Fore.RESET
            case code if 500 <= code <= 599:
                status = Fore.RED + "Server error" + Fore.RESET
            case _:
                status = "Unknown code" + Fore.RESET

        #Создание строки в таблице на основе полученных данных
        monitorTable.add_row([argv[i], response.elapsed.total_seconds(), response.status_code, status])

    #Отчистка окна терминала
    print("\033[H\033[J")
    #Вывод таблицы на экран
    print(monitorTable)

    #Вывод логов в файл
    logging.basicConfig(level=logging.DEBUG, filename = "mylog.log", format = "%(asctime)s -- %(message)s", datefmt='%H:%M:%S')
    logging.info(monitorTable)
