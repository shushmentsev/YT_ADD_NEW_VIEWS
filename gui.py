# -*- coding: utf-8 -*-

from tkinter import Tk, Button, StringVar, Entry
from add_views import add_views

def crt_gui(**data):

    # Получение переменных:
    drv = data.get('drv')

    # Настройка окна:
    win = Tk()
    win.geometry("600x200")
    win.title("Программа для накрутки просмотров")
    win.resizable(width=False, height=False)

    # Поле для ввода поискового запроса:
    global var_req
    var_req = StringVar()
    ent_req = Entry(win, textvariable=var_req)  
    ent_req.place(anchor="nw", relx=0.0, y=0, relwidth=0.8, height=25)

    # Поле для ввода времени 0:
    global var_time_0
    var_time_0 = StringVar()
    ent_time_0 = Entry(win, textvariable=var_time_0)  
    ent_time_0.place(anchor="nw", relx=0.05, y=25, relwidth=0.05, height=25)

    # Поле для ввода времени 1:
    global var_time_1
    var_time_1 = StringVar()
    ent_time_1 = Entry(win, textvariable=var_time_1)  
    ent_time_1.place(anchor="nw", relx=0.15, y=25, relwidth=0.05, height=25)

    # Поле для ввода времени 2:
    global var_time_2
    var_time_2 = StringVar()
    ent_time_2 = Entry(win, textvariable=var_time_2)  
    ent_time_2.place(anchor="nw", relx=0.25, y=25, relwidth=0.05, height=25)

    # Поле для ввода времени 3:
    global var_time_3
    var_time_3 = StringVar()
    ent_time_3 = Entry(win, textvariable=var_time_3)  
    ent_time_3.place(anchor="nw", relx=0.35, y=25, relwidth=0.05, height=25)

    # Поле для ввода времени 4:
    global var_time_4
    var_time_4 = StringVar()
    ent_time_4 = Entry(win, textvariable=var_time_4)  
    ent_time_4.place(anchor="nw", relx=0.45, y=25, relwidth=0.05, height=25)

    # Поле для ввода времени 5:
    global var_time_5
    var_time_5 = StringVar()
    ent_time_5 = Entry(win, textvariable=var_time_5)  
    ent_time_5.place(anchor="nw", relx=0.55, y=25, relwidth=0.05, height=25)

    # Поле для ввода времени 6:
    global var_time_6
    var_time_6 = StringVar()
    ent_time_6 = Entry(win, textvariable=var_time_6)  
    ent_time_6.place(anchor="nw", relx=0.65, y=25, relwidth=0.05, height=25)

    # Поле для ввода времени 7:
    global var_time_7
    var_time_7 = StringVar()
    ent_time_7 = Entry(win, textvariable=var_time_7)  
    ent_time_7.place(anchor="nw", relx=0.75, y=25, relwidth=0.05, height=25)

    # Поле для ввода времени 8:
    global var_time_8
    var_time_8 = StringVar()
    ent_time_8 = Entry(win, textvariable=var_time_8)  
    ent_time_8.place(anchor="nw", relx=0.85, y=25, relwidth=0.05, height=25)

    # Поле для ввода времени 9:
    global var_time_9
    var_time_9 = StringVar()
    ent_time_9 = Entry(win, textvariable=var_time_9)  
    ent_time_9.place(anchor="nw", relx=0.95, y=25, relwidth=0.05, height=25)

    # Поле для ввода количества повторов:
    global var_count
    var_count = StringVar()
    ent_count = Entry(win, textvariable=var_count)
    ent_count.place(anchor="nw", relx=0.55, y=50, relwidth=0.35, height=25)

    # Кнопка "Накрутить":
    var_list = [var_time_0, var_time_1, var_time_2, var_time_3, var_time_4, var_time_5, var_time_6, var_time_7,
                var_time_8, var_time_9, drv, var_req, var_count]
    btn_start = Button(win, text="Накрутить", command=lambda: add_views(var_list))
    btn_start.place(anchor="nw", relx=0.8, y=0, relwidth=0.2, height=25)



    # Mainloop():
    win.mainloop()
    
if __name__ == '__main__':

    from drv import get_drv
    drv_1 = get_drv()
    crt_gui(drv=drv_1)

