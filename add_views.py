# -*- coding: utf-8 -*-

def add_views(var_list):

    # Подключение библиотек:
    from time import sleep
    from selenium.webdriver.common.keys import Keys

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

    # Переход по ссылке:
    drv.get(url)
    #elem = drv.find_element_by_class_name('html5-video-container')
    elem = drv.find_element_by_tag_name('body')
    print(elem)
    sleep(5)
    elem.send_keys(Keys.ESCAPE)
    sleep(1)
    elem.send_keys('3')
    sleep(1)
    elem.send_keys('9')


if __name__ == '__main__':

    pass
