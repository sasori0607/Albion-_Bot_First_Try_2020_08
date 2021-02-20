import pyautogui
import numpy as np
import cv2
import time
from tkinter import *
import threading
import ctypes
import sys

user32 = ctypes.windll.user32

#проверка для ДЕФ на стоп
def proverka():#хня СЮДАААААААААААААА
    global T
    if T < 2:
        return sys.exit()
    xx = threading.Thread(target=proverka3aBuCaHu9l, args=())
    xx.start()

def proverka3aBuCaHu9l():
    global start_time
    t = (time.time() - start_time)
    print(t)
    if t > 80:
        print("Зависла шарманка")
        ALL_OFF()
        time.sleep(5)
        xx = threading.Thread(target=thread_re_3aBuCaHu9l, args=())
        xx.start()
        return sys.exit()

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
    threshold = 0.25#0.3 стандарт
    screen = pyautogui.screenshot(region=(qwer[0]+oknoP[0], qwer[1]+oknoP[1], qwer[2], qwer[3]))
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
    time.sleep(0.10)
    while x == 0:
        z=screen
        x=1
    while x == 1:
        screen = pyautogui.screenshot(region=(qwer[0]+oknoP[0], qwer[1]+oknoP[1], qwer[2], qwer[3]))
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(screen, z, cv2.TM_CCOEFF_NORMED)
        z=screen
        time.sleep(0.07)
        proverka()
        if res < threshold :
            x=2
            print("поплавок двинулся")
        else:
            print("ожидаем поплавок")
#поиск коордтнат игры
def GAMEkord():#поиск координат поплавка
    x=0
    src_rgb = cv2.imread('image_GAME.png')
    src_gray = cv2.cvtColor(src_rgb, cv2.COLOR_BGR2GRAY)

    while x==0:
        screen = pyautogui.screenshot(region=(0, 0, 1919, 1079))
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
        #коорды
        w, h = src_gray.shape[::-1]
        res = cv2.matchTemplate(screen, src_gray, cv2.TM_CCOEFF_NORMED)

        threshold = 0.75

        loc = np.where( res >= threshold)
        proverka()
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (250,0,255), 1)
            print("поиск игры")
            #cv2.imwrite('res.png',screen)
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
    threshold2 = 0.75#0.5
    screen = pyautogui.screenshot(region=(qwerty[0]+10,qwerty[1]+27,40,2))
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
    time.sleep(0.18)
    while x == 0:
        zx=screen[1, 30]
        z=screen
        x = 1
        #print(z[x, y])
        cv2.imwrite('res.png', screen)
    while x == 1:

        screen = pyautogui.screenshot(region=(qwerty[0]+10,qwerty[1]+27,40,2))
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)

        res = cv2.matchTemplate(screen, z, cv2.TM_CCOEFF_NORMED)
        #z = screen
        time.sleep(0.01)
        #cv2.imwrite('res.png', screen)

        if res < threshold2:
            print("идет игра", res)
            pyautogui.mouseUp(button='left')
            time.sleep(0.20)
            print(screen[1, 30])
            x=Off(zx,screen)
        else:
            print("идет игра Гзона", res)
            pyautogui.mouseDown(button='left')
            time.sleep(0.08)
            print(screen[1, 30])
            x=Off(zx,screen)
#проверка закончина ли игра
def Off(zx,screen):
    proverka()
    if zx-2 < screen[1, 30] < zx+2:
        print('nice')
        x = 1
        return (x)
    else:
        print('off')
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
    src_rgb = cv2.imread('image_fragmentX2.png')
    src_gray = cv2.cvtColor(src_rgb, cv2.COLOR_BGR2GRAY)
    while T > -2:

        print('jDem')
        if c3>0:
                proverka2()
                screen = pyautogui.screenshot(region=(0, 0,user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)))
                screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
                # коорды
                w, h = src_gray.shape[::-1]
                res = cv2.matchTemplate(screen, src_gray, cv2.TM_CCOEFF_NORMED)

                threshold = 0.999

                loc = np.where(res >= threshold)
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (250, 0, 255), 1)
                    print("Нашли засранца")
                    cv2.imwrite('resSCAN.png', screen)
                    FFF()
                    time.sleep(6)
                else:
                    print("засранца не нашли")
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
    #c2.var.Value = True
   # var.setChecked(True)
    var.set(True)


    root.mainloop()



start_time = 0
T = -5 #ключ переменная, отвечает за проверку+запуск
c3=2#коюч к  scanpleyr()
oknoP=0#глобализация переменной для функции рыбалки
qwer=0#глобализация переменной для функции рыбалки
qwerty=0#глобализация переменной для функции рыбалки

#код начало бота
xx = threading.Thread(target=thread_function, args=())
xx.start()








