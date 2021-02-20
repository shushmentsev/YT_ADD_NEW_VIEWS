# -*- coding: utf-8 -*-

def crt_gui(**data):

    # Библиотеки:
    from tkinter import Tk, Button, Label, Entry, StringVar
    from add_views import add_views

    # Получение переменных:
    drv = data.get('drv')

    # Настройка окна:
    win = Tk()
    win.geometry("600x81")
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
    ent_time_0.place(anchor="nw", relx=0.05, y=27, relwidth=0.05, height=25)

    # Поле для ввода времени 1:
    global var_time_1
    var_time_1 = StringVar()
    ent_time_1 = Entry(win, textvariable=var_time_1)  
    ent_time_1.place(anchor="nw", relx=0.15, y=27, relwidth=0.05, height=25)

    # Поле для ввода времени 2:
    global var_time_2
    var_time_2 = StringVar()
    ent_time_2 = Entry(win, textvariable=var_time_2)  
    ent_time_2.place(anchor="nw", relx=0.25, y=27, relwidth=0.05, height=25)

    # Поле для ввода времени 3:
    global var_time_3
    var_time_3 = StringVar()
    ent_time_3 = Entry(win, textvariable=var_time_3)  
    ent_time_3.place(anchor="nw", relx=0.35, y=27, relwidth=0.05, height=25)

    # Поле для ввода времени 4:
    global var_time_4
    var_time_4 = StringVar()
    ent_time_4 = Entry(win, textvariable=var_time_4)  
    ent_time_4.place(anchor="nw", relx=0.45, y=27, relwidth=0.05, height=25)

    # Поле для ввода времени 5:
    global var_time_5
    var_time_5 = StringVar()
    ent_time_5 = Entry(win, textvariable=var_time_5)  
    ent_time_5.place(anchor="nw", relx=0.55, y=27, relwidth=0.05, height=25)

    # Поле для ввода времени 6:
    global var_time_6
    var_time_6 = StringVar()
    ent_time_6 = Entry(win, textvariable=var_time_6)  
    ent_time_6.place(anchor="nw", relx=0.65, y=27, relwidth=0.05, height=25)

    # Поле для ввода времени 7:
    global var_time_7
    var_time_7 = StringVar()
    ent_time_7 = Entry(win, textvariable=var_time_7)  
    ent_time_7.place(anchor="nw", relx=0.75, y=27, relwidth=0.05, height=25)

    # Поле для ввода времени 8:
    global var_time_8
    var_time_8 = StringVar()
    ent_time_8 = Entry(win, textvariable=var_time_8)  
    ent_time_8.place(anchor="nw", relx=0.85, y=27, relwidth=0.05, height=25)

    # Поле для ввода времени 9:
    global var_time_9
    var_time_9 = StringVar()
    ent_time_9 = Entry(win, textvariable=var_time_9)  
    ent_time_9.place(anchor="nw", relx=0.95, y=27, relwidth=0.05, height=25)

    # Поле для ввода количества повторов:
    global var_count
    var_count = StringVar()
    ent_count = Entry(win, textvariable=var_count)
    ent_count.place(anchor="nw", relx=0.35, y=54, relwidth=0.1, height=25)

    # Кнопка "Накрутить":
    var_list = [var_time_0, var_time_1, var_time_2, var_time_3, var_time_4, var_time_5, var_time_6, var_time_7,
                var_time_8, var_time_9, drv, var_req, var_count]
    btn_start = Button(win, text="Накрутить", command=lambda: add_views(var_list))
    btn_start.place(anchor="nw", relx=0.8, y=0, relwidth=0.2, height=25)

    # Надпись '0:'
    lbl_0 = Label(win, text='0:')
    lbl_0.place(anchor="nw", relx=0.0, y=27, relwidth=0.05, height=25)

    # Надпись '1:'
    lbl_1 = Label(win, text='1:')
    lbl_1.place(anchor="nw", relx=0.1, y=27, relwidth=0.05, height=25)

    # Надпись '2:'
    lbl_2 = Label(win, text='2:')
    lbl_2.place(anchor="nw", relx=0.2, y=27, relwidth=0.05, height=25)

    # Надпись '3:'
    lbl_3 = Label(win, text='3:')
    lbl_3.place(anchor="nw", relx=0.3, y=27, relwidth=0.05, height=25)

    # Надпись '4:'
    lbl_4 = Label(win, text='4:')
    lbl_4.place(anchor="nw", relx=0.4, y=27, relwidth=0.05, height=25)

    # Надпись '5:'
    lbl_5 = Label(win, text='5:')
    lbl_5.place(anchor="nw", relx=0.5, y=27, relwidth=0.05, height=25)

    # Надпись '6:'
    lbl_6 = Label(win, text='6:')
    lbl_6.place(anchor="nw", relx=0.6, y=25, relwidth=0.05, height=25)

    # Надпись '7:'
    lbl_7 = Label(win, text='7:')
    lbl_7.place(anchor="nw", relx=0.7, y=27, relwidth=0.05, height=25)

    # Надпись '8:'
    lbl_8 = Label(win, text='8:')
    lbl_8.place(anchor="nw", relx=0.8, y=27, relwidth=0.05, height=25)

    # Надпись '9:'
    lbl_9 = Label(win, text='9:')
    lbl_9.place(anchor="nw", relx=0.9, y=27, relwidth=0.05, height=25)

    # Надпись 'Количество новых просмотров:'
    lbl_9 = Label(win, text='Количество новых просмотров:')
    lbl_9.place(anchor="nw", relx=0.0, y=54, relwidth=0.35, height=25)

    # Mainloop():
    win.mainloop()
    
if __name__ == '__main__':

    from drv import get_drv
    drv_1 = get_drv()
    crt_gui(drv=drv_1)
