# coding: utf-8

# Python. Быстрый старт.
# Занятие 8.

# Домашнее задание: 
#       в модуле робота создать функцию удаления случайного файла из указанной директории;
#       при проигрыше сделать случайный выбор наказания - либо дублирование файлов, либо удаление файла.


import turtle
# import tkSimpleDialog   # 2.x Python
import random
import math

import mrrobot

PHI = 360 / 7
R = 50


def gotoxy(x, y):       # функция перемещения пера
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(r, color):      # функция рисования закрашенного круга
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def draw_pistol(base_x, base_y):
    # основной круг
    gotoxy(base_x, base_y)
    turtle.circle(80)
    # мушка
    gotoxy(base_x, base_y + 160)
    draw_circle(5, "red")

    # барабан
    for i in range(0, 7):  # random.randrange(7,100)
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, "white")


def rotate_pistol(base_x, base_y, start):
    for i in range(start, random.randrange(7, 100)):  # random.randrange(7,100)
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, "brown")
        draw_circle(22, "white")

    gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
    draw_circle(22, "brown")

    return i % 7


turtle.speed(0)
turtle.hideturtle()
draw_pistol(100, 100)

answer = ''
start = 0
while answer != 'N':
    answer = turtle.textinput("Играть?", "Y/N")
    # tkSimpleDialog.askstring("Нарисовать окружность", "Y/N")       # for 2.x Python

    if answer == 'Y':
        start = rotate_pistol(100, 100, start)

        start = 0
        if start == 0:
            gotoxy(-150, 250)
            turtle.write("Вы проиграли!", font=("Arial", 18, "normal"))

            z = random.randrange(0, 3)
            if z < 2:
                gotoxy(-100, -100)
                dirname = turtle.textinput("Ввод", "Укажите имя директории:")
            if z == 0:
                mrrobot.duble_files(dirname)
            elif z == 1:
                mrrobot.random_delete(dirname)
            else:
                gotoxy(-100, -50)
                turtle.write("Вам везёт!", font=("Arial", 20, "normal"))

    else:
        gotoxy(-75, -50)
        turtle.write("Введите Y или N")
