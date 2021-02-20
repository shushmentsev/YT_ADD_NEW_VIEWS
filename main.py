# -*- coding: utf-8 -*-

from drv import get_drv
from gui import crt_gui

if __name__ == '__main__':

    drv_1 = get_drv()
    crt_gui(drv=drv_1)
