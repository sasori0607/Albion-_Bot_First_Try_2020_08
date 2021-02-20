import pyautogui
import numpy as np
import cv2
import time
from tkinter import *
import threading
import ctypes
import sys
from licensing.methods import Key, Helpers
user32 = ctypes.windll.user32
import keyboard

#проверка для ДЕФ на стоп
def proverka():#хня СЮДАААААААААААААА
    global gaber
    global T
    if T < 2:
        return sys.exit()
    gaber=gaber+1
    if gaber ==10:
        xx = threading.Thread(target=proverka3aBuCaHu9l, args=())
        xx.start()
        gaber = 0

def proverka3aBuCaHu9l():

    global start_time
    t = (time.time() - start_time)
    print(t)
    if t > 85:
        print("Зависла шарманка")
        ALL_OFF()
        time.sleep(5)
        rr=BuLeT()
        if rr == 10:
            xx = threading.Thread(target=thread_re_3aBuCaHu9l, args=())
            xx.start()
            return sys.exit()
        else:
            xx = threading.Thread(target=pere3axoD, args=())
            xx.start()
            return sys.exit()

def pere3axoD(oknoP) :
    time.sleep(3)
    pyautogui.moveTo(oknoP[0]+500, oknoP[1]+485)
    time.sleep(1.5)
    pyautogui.mouseDown(button='left')
    time.sleep(0.7)
    pyautogui.mouseUp(button='left')
    time.sleep(20)
    pyautogui.moveTo(oknoP[0]+510, oknoP[1]+630)
    pyautogui.mouseDown(button='left')
    time.sleep(0.7)
    pyautogui.mouseUp(button='left')
    time.sleep(20)
    pyautogui.typewrite(['esc'])
    time.sleep(0.7)
    pyautogui.typewrite(['esc'])
    time.sleep(0.7)
    pyautogui.typewrite(['esc'])
    time.sleep(0.7)
    FF()


def BuLeT():
    x = 0
    path = r'knopka.png'
    rgb = cv2.imread(path)
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    if x == 0:
        screen = pyautogui.screenshot(region=(0, 0, user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)))
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
        # коорды
        w, h = gray.shape[::-1]
        res = cv2.matchTemplate(screen, gray, cv2.TM_CCOEFF_NORMED)

        threshold = 0.85
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (250, 0, 255), 1)
            print("Вылет")
            cv2.imwrite('res.png', screen)
            #gghh1= loc[1][0]
            #gghh2= loc[0][0]
            xx = threading.Thread(target=pere3axoD(oknoP), args=())
            xx.start()

            # получаемые знач
            return 5
            break
        else:
            print("Вылета нету, играем")
            time.sleep(0.1)
            return 10

def thread_re_3aBuCaHu9l():
    e=0
    while e<5:
        time.sleep(2.5)
        e=e+1
    FF()

def proverka2():
    global T
    if T < -1:
        return exit()
#поиск окна по иконке
def okno():
    x = 0
    path = r'image_fragmentX.png'
    rgb = cv2.imread(path)
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    while x == 0:
        proverka()
        screen = pyautogui.screenshot(region=(0, 0, user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)))
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
        # коорды
        w, h = gray.shape[::-1]
        res = cv2.matchTemplate(screen, gray, cv2.TM_CCOEFF_NORMED)

        threshold = 0.85
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (250, 0, 255), 1)
            print("окно найденно")
            cv2.imwrite('res.png',screen)
            x = 2
            # получаемые знач
            return (loc[1][0]), (loc[0][0])
            print("получилиКорды")
            break
        else:
            print("ищем окно",T)
            time.sleep(0.1)
#поиск поплавка на экране
def poplavok():#поиск координат поплавка
    x=0
    src_rgb = cv2.imread('image_fragment.png')
    src_gray = cv2.cvtColor(src_rgb, cv2.COLOR_BGR2GRAY)

    while x==0:
        screen = pyautogui.screenshot(region=(oknoP[0], oknoP[1], 1024, 768))
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
        #коорды
        w, h = src_gray.shape[::-1]
        res = cv2.matchTemplate(screen, src_gray, cv2.TM_CCOEFF_NORMED)

        threshold = 0.77

        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (250,0,255), 1)
            print("++")
            cv2.imwrite('res.png',screen)
            x=2
            #получаемые знач
            return  (loc[1][0] ), (loc[0][0]  ),w,h
            print("получилиКорды")
            proverka()
            break
        else:
            proverka()
            print("-")
#проверка движения поплавка
def scan():
    x = 0
    threshold = 0.15#0.3 стандарт0.25############################################тут
    screen = cv2.imread('image_fragment.png')
    #screen = pyautogui.screenshot(region=(qwer[0]+oknoP[0], qwer[1]+oknoP[1], qwer[2], qwer[3]))
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
    #time.sleep(0.10)
    while x == 0:
        z=screen
        x=1
    while x == 1:
        screen = pyautogui.screenshot(region=(qwer[0]+oknoP[0], qwer[1]+oknoP[1], qwer[2], qwer[3]))
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(screen, z, cv2.TM_CCOEFF_NORMED)
        z=screen
        #time.sleep(0.07)
        proverka()
        if res < threshold :
            x=2
            print("поплавок двинулся",res)
        else:
            print("ожидаем поплавок")
#поиск коордтнат игры
def GAMEkord():#поиск координат поплавка игры
    x=0
    src_rgb = cv2.imread('image_GAME.png')
    src_gray = cv2.cvtColor(src_rgb, cv2.COLOR_BGR2GRAY)

    while x==0:
        screen = pyautogui.screenshot(region=(oknoP[0], oknoP[1], 1024, 768))
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
        #коорды
        w, h = src_gray.shape[::-1]
        res = cv2.matchTemplate(screen, src_gray, cv2.TM_CCOEFF_NORMED)

        threshold = 0.75#0.75

        loc = np.where( res >= threshold)
        proverka()
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (250,0,255), 1)
            print("поиск игры")
            cv2.imwrite('resQQ.png',screen)
            x=2
            #получаемые знач
            print(pt[1] + h)
            return  (loc[1][0] ), (loc[0][0]  ),w,h
            break
        else:
            print("-")
#процес игры по заданным координатам
def GAMEgreen():
    x = 0
    ii = 0
    threshold2 = 0.60#0.5
    x3HAX=oknoP[0]+qwerty[0]
    x3HAX2=oknoP[1]+qwerty[1]
    screen = pyautogui.screenshot(region=(x3HAX+10,x3HAX2+21,50,1))
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
    while x == 0:
        zx=screen[0, 49]
        z=screen
        x = 1
        #print(z[x, y])
        cv2.imwrite('res.png', screen)
    while x == 1:

        screen = pyautogui.screenshot(region=(x3HAX+10,x3HAX2+21,50,1))
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)

        res = cv2.matchTemplate(screen, z, cv2.TM_CCOEFF_NORMED)
        #z = screen
        #time.sleep(0.005)
        #cv2.imwrite('res.png', screen)

        if res < threshold2:
            print("идет играВЕРХ", res)
            pyautogui.mouseUp(button='left')
            time.sleep(0.01)#0.05
            print(screen[0, 39])
            ii = 0
            x=Off(zx,screen)
        else:
            print("идет играНИЗ", res)
            if ii == 0:
                pyautogui.mouseDown(button='left')
                ii = 1
            #time.sleep(0.04)#0.03#0.22
            #print(screen[0, 39])
            x=Off(zx,screen)
#проверка закончина ли игра
def Off(zx,screen):
    proverka()
    if zx-2 < screen[0, 49] < zx+2:
        print('nice')
        x = 1
        return (x)
    else:
        print('off',screen[0, 49])
        x = 2
        pyautogui.mouseUp(button='left')
        return (x)
#скрипт нажатия кнопки старт увелеченние переменной
def FF():
 global T
 T = 4
 xx = threading.Thread(target=thread_functionS, args=())
 xx1 = threading.Thread(target=scanpleyr, args=())
 xx1.start()
 xx.start()
 return T
#скрипт  уменьшения(до0) переменной(1lvl)
def FFF():

    global T
    T=0
    print(T)

#уродство реализации чекбокса

def FFFF():
    global c3
    if c3 == 2:
        print("1-1")
        c3=0
    elif c3 == 0:
        print("0+1")
        c3=2
#процес скана с чекбокса
def scanpleyr():
    global T
    src_rgb = cv2.imread('image_fragmentX22.png')
    src_gray = cv2.cvtColor(src_rgb, cv2.COLOR_BGR2GRAY)
    while T > -2:

        print('jDem')
        if c3>0:
            if oknoP != 0:
                proverka2()
                screen = pyautogui.screenshot(region=(oknoP[0], oknoP[1], 1024, 768))
                screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
                # коорды
                w, h = src_gray.shape[::-1]
                res = cv2.matchTemplate(screen, src_gray, cv2.TM_CCOEFF_NORMED)

                threshold = 0.80

                loc = np.where(res >= threshold)
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (250, 0, 255), 1)
                    print("Нашли засранца")
                    cv2.imwrite('resSCAN.png', screen)
                    T = T - 4
                    time.sleep(6)
                else:
                    print("засранца не нашли",loc)
                    time.sleep(5)
                    T = T + 1
                    if T==3:
                        xx = threading.Thread(target=thread_functionS, args=())
                        xx.start()


        time.sleep(2)
#скрипт нажатия кнопки старт уменьшения(до-5) переменной(2lvl)
def ALL_OFF():
    global T
    T=-5

def okno_exit():
    root = Tk()
    root['bg'] = '#fafafa'
    # Указываем название окна
    root.title('Погодное приложение')
    # Указываем размеры окна
    root.geometry('350x150')
    # Делаем невозможным менять размеры окна
    root.resizable(width=False, height=False)

    lbl = Label(root, text="Неверный ключ или он истек ",bg='#fafafa', font=("Arial Bold", 16))
    lbl.grid(column=0, row=100)
    lbl.place(relx=0.03, rely=0.10, relwidth=0.94, relheight=0.17)
    btn2 = Button(root, text='Выхожу', bg='red', font=40, command=exit)
    btn2.place(relx=0.2, rely=0.30, relwidth=0.60, relheight=0.4)
    root.mainloop()








#???функция игры
def thread_functionS():
        while T>0:
            global oknoP
            global qwer
            global qwerty
            global start_time
            start_time = time.time()
            oknoP=okno()
            print(oknoP)
            pyautogui.moveTo(oknoP[0] + 500, oknoP[1] + 150)
            pyautogui.mouseDown(button='right')
            time.sleep(0.1)
            pyautogui.mouseUp(button='right')
            pyautogui.moveTo(oknoP[0] + 500, oknoP[1] + 150)
            time.sleep(1.5)
            pyautogui.mouseDown(button='left')
            time.sleep(1.7)
            pyautogui.mouseUp(button='left')
            qwer = poplavok()
            print(qwer)
            scan()
            pyautogui.moveTo(qwer[0] + oknoP[0], qwer[1] + oknoP[1])
            pyautogui.mouseDown(button='left')
            time.sleep(0.01)
            pyautogui.mouseUp(button='left')
            time.sleep(0.09)
            qwerty = GAMEkord()
            time.sleep(0.01)
            GAMEgreen()
            time.sleep(2)

        else:
            print("GDEM")
#сам интерфейс +кнопки
def thread_function():
    root = Tk()
    root['bg'] = '#fafafa'
    # Указываем название окна
    root.title('Погодное приложение')
    # Указываем размеры окна
    root.geometry('200x350')
    # Делаем невозможным менять размеры окна
    root.resizable(width=False, height=False)
    btn1 = Button(root, text='Начать', bg='green' ,font=40, command=FF)
    btn1.place(relx=0.05, rely=0.10, relwidth=0.40, relheight=0.1)

    btn2 = Button(root, text='Стоп',bg='red' ,font=40,command=ALL_OFF)
    btn2.place(relx=0.55, rely=0.10, relwidth=0.40, relheight=0.1)

    var = BooleanVar()
    var.set(0)
    c2 = Checkbutton(text="Вкл/Выкл скана игроков",bg='#fafafa',command=FFFF,variable=var)
    c2.place(relx=0.01, rely=0.30, relwidth=0.90, relheight=0.08)
    #список выпадающий. variable.get() получения знач
    OPTIONS = [
        "Верхняя часть экрана",
        "Feb",
        "Mar"
    ]  # etc
    variable = StringVar(root)
    variable.set(OPTIONS[0])  # default value
    w = OptionMenu(root, variable, *OPTIONS)
    w.pack()
    w.place(relx=0.01, rely=0.80, relwidth=0.90, relheight=0.08)


    var.set(True)


    root.mainloop()



start_time = 0
T = -5 #ключ переменная, отвечает за проверку+запуск
c3=2#коюч к  scanpleyr()
oknoP=0#глобализация переменной для функции рыбалки
qwer=0#глобализация переменной для функции рыбалки
qwerty=0#глобализация переменной для функции рыбалки
gaber = 0#проверка вылета успокоительное


RSAPubKey = "<RSAKeyValue><Modulus>i0GXJBEtPu1FOOytorBIIp5ZJA8zwRQoYxBjlOmZL4bqcICbHAm3v36Foj8YPCee04ixWjEyoZP5AuGv2rPup9omqo8srXbexQHiNaav3tru0GkrOl6MmXczOwXHybAjbc2xcwAKOagjS704AtTn4y6pFjbNppdyeTS+oUvTwcxQRdj/73iIWsb3hiUfHsr8/iIgETqc1eoU9zZkSBK1zEBL4P5yaYYstHfsICRzgjwPZltgFgoqV0myirejepfaDPDRwohBVnxX3DlDHZD4/lxxtvUTx2S5eNFwPJnjq4/SJonOuDMONTwfeeLOEvLUUALsi02ewFIz2Rj7f6C5TQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI2MTQ0NiIsIi9kQjdsdng3ZW5JbTl2aVBEN1RoNXZtKzR5MXNOTE8xNTZrNHdwbXoiXQ =="
listkey = open('list.txt')
listkey = listkey.read()

result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=7164, \
                   key=listkey,\
                   machine_code=Helpers.GetMachineCode())

if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
    # an error occurred or the key is invalid or it cannot be activated
    # (eg. the limit of activated devices was achieved)
    print("The license does not work: {0}".format(result[1]))
    #ВЫключение проверки и дополнения автовыхода
    #xx = threading.Thread(target=okno_exit, args=())


    xx = threading.Thread(target=thread_function, args=())
    xx.start()
    #////////////////
    key = 'F12'
    while True:
        if keyboard.is_pressed(key):
            print('rkf')
            ALL_OFF()
    #//////////////
else:
    # код начало бота
    xx = threading.Thread(target=thread_function, args=())
    xx.start()
    key = 'F12'
    while True:
        if keyboard.is_pressed(key):
            print('rkf')
            ALL_OFF()









