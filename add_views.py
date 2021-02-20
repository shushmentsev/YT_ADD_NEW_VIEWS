# -*- coding: utf-8 -*-

def add_views(var_list):

    # Подключение библиотек:
    from time import sleep
    from selenium.webdriver.common.keys import Keys
    from time import monotonic

    # Получение переменных:
    time_0 = var_list[0].get()
    time_1 = var_list[1].get()
    time_2 = var_list[2].get()
    time_3 = var_list[3].get()
    time_4 = var_list[4].get()
    time_5 = var_list[5].get()
    time_6 = var_list[6].get()
    time_7 = var_list[7].get()
    time_8 = var_list[8].get()
    time_9 = var_list[9].get()
    drv = var_list[10]
    url = var_list[11].get()
    count = int(var_list[12].get())

    for i in range(count):

        # Переход по ссылке:
        drv.get('https://www.google.com')
        drv.get(url)
        #elem = drv.find_element_by_class_name('html5-video-container')
        elem = drv.find_element_by_tag_name('body')
        print(elem)
        sleep(5)
        elem.send_keys(Keys.ESCAPE)
        sleep(5)

        # TODO: Проверка на числа

        # 0 Часть:
        if time_0 != '':

            elem.send_keys('0')
            t_1 = monotonic()

            while True:
                if (monotonic() - t_1) < float(time_0):
                    sleep(1)
                elif (monotonic() - t_1) >= float(time_0):
                    print('Всё')
                    break
        # 1 Часть:
        if time_1 != '':

            elem.send_keys('1')
            t_1 = monotonic()

            while True:
                if (monotonic() - t_1) < float(time_1):
                    sleep(1)
                elif (monotonic() - t_1) >= float(time_1):
                    print('Всё')
                    break
        # 2 Часть:
        if time_2 != '':

            elem.send_keys('2')
            t_1 = monotonic()

            while True:
                if (monotonic() - t_1) < float(time_2):
                    sleep(1)
                elif (monotonic() - t_1) >= float(time_2):
                    print('Всё')
                    break


        # 3 Часть:
        if time_3 != '':

            elem.send_keys('3')
            t_1 = monotonic()

            while True:
                if (monotonic() - t_1) < float(time_3):
                    sleep(1)
                elif (monotonic() - t_1) >= float(time_3):
                    print('Всё')
                    break

        # 4 Часть:
        if time_4 != '':

            elem.send_keys('4')
            t_1 = monotonic()

            while True:
                if (monotonic() - t_1) < float(time_4):
                    sleep(1)
                elif (monotonic() - t_1) >= float(time_4):
                    print('Всё')
                    break

        # 5 Часть:
        if time_5 != '':

            elem.send_keys('5')
            t_1 = monotonic()

            while True:
                if (monotonic() - t_1) < float(time_5):
                    sleep(1)
                elif (monotonic() - t_1) >= float(time_5):
                    print('Всё')
                    break

        # 6 Часть:
        if time_6 != '':

            elem.send_keys('6')
            t_1 = monotonic()

            while True:
                if (monotonic() - t_1) < float(time_6):
                    sleep(1)
                elif (monotonic() - t_1) >= float(time_6):
                    print('Всё')
                    break

        # 7 Часть:
        if time_7 != '':

            elem.send_keys('7')
            t_1 = monotonic()

            while True:
                if (monotonic() - t_1) < float(time_7):
                    sleep(1)
                elif (monotonic() - t_1) >= float(time_7):
                    print('Всё')
                    break

        # 8 Часть:
        if time_8 != '':

            elem.send_keys('8')
            t_1 = monotonic()

            while True:
                if (monotonic() - t_1) < float(time_8):
                    sleep(1)
                elif (monotonic() - t_1) >= float(time_8):
                    print('Всё')
                    break

        # 9 Часть:
        if time_9 != '':

            elem.send_keys('9')
            t_1 = monotonic()

            while True:
                if (monotonic() - t_1) < float(time_9):
                    sleep(1)
                elif (monotonic() - t_1) >= float(time_9):
                    print('Всё')
                    break


if __name__ == '__main__':

    pass
