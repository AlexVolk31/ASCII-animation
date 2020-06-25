import time  # Библиотека для работы со временем
import os  # Библиотека для работы с системой

def getready(place, NoF):
    mas = []
    for i in range(NoF):
        string = place+r'\ASCII-'+str(i)+'.txt'
        print(place+r'\ASCII-'+str(i)+'.txt')
        file = open(place+r'\ASCII-'+str(i)+'.txt', 'rt')
        mas.append(file.read())
        print(file.read())
    return mas

#C:\Users\AlexVolk\Desktop\animations\sign'

def main(n):
    directory = r'animations\sign'
    frames = getready(directory, 25)
    for frame in frames * n:
        os.system('cls')  # Очистка экрана перед новым кадром
        print(frame, end='')  # Отрисовка самого кадра
        time.sleep(1 / 60)  # Задержка для плавносли отрисовки

main(1000)
