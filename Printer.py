import time  # Библиотека для работы со временем
import os  # Библиотека для работы с системой


def interface(place):
    mas = []
    info = -1
    print(*os.listdir(place),sep=' <- ', end=' <-\n')
    while info==-1:
        try:
            inputplace = place + '\\' + input('Введите название анимации из списка:\n')
            info = len(os.listdir(inputplace))
        except :
            print("Неверное имя файла")
    for i in range(info):
        file = open(inputplace + r'\ASCII-' + str(i) + '.txt', 'rt')
        mas.append(file.read())
    return mas

def animation(frames):
    while True:
        for frame in frames:
            os.system('cls')  # Очистка экрана перед новым кадром
            print(frame, end='')  # Отрисовка самого кадра
            time.sleep(1 / (len(frames)+30))  # Задержка для плавносли отрисовки

def getready(place):
    mas = []
    print(os.listdir(r'animations'))
    for i in range(NoF):
        file = open(place+r'\ASCII-'+str(i)+'.txt', 'rt')
        mas.append(file.read())
    return mas



def main():
    directory = 'animations'
    while True:
        try:
            inputframes = interface(directory)
            print("Для остановки анимации нажмите Ctrl+C")
            time.sleep(2)
            animation(inputframes)
        except KeyboardInterrupt:
            pass





main()
