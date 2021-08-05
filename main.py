# -*- coding: utf-8 -*-

from os import system
from drv import get_drv
from gui import crt_gui


if __name__ == '__main__':

    # Запуск браузера с определённым профилем:
    system('start chrome.exe -remote-debugging-port=9014 --user-data-dir="D:\Selenium\Test_1"')

    drv_1 = get_drv()
    crt_gui(drv=drv_1)
