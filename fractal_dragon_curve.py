import turtle
# библиотека для работы с цветами
import colorsys

screen = turtle.Screen()
screen.bgcolor("white")

# скорость анимации
screen.tracer(2)

turtle_ = turtle.Turtle()

# цветовой режим от 0 до 1
turtle.colormode(1)
# толщина линии
turtle_.pensize(2)
# скрываем черепаху (курсор, который рисует фигуру)
turtle_.hideturtle()

# перемещаемся в стартовую позицию
turtle_.penup()
turtle_.goto(-300, 0)
turtle_.pendown()

# счётчик шагов (для цвета)
step = 0

# функция кривой дракона
def dragon_curve(length, depth, direction, max_depth):
    global step

    # если дошли до конца рекурсии
    if depth == 0:
        # вычисляем цвет по номеру шага
        hue = (step % 360) / 360
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        # устанавливаем цвет линии
        turtle_.pencolor(r, g, b)
        # рисуем отрезок
        turtle_.forward(length)
        # увеличиваем счётчик
        step += 1
        return
    # левая версия
    if direction == 1:
        turtle_.left(45)
        dragon_curve(length / 1.414, depth - 1, 1, max_depth)
        turtle_.right(90)
        dragon_curve(length / 1.414, depth - 1, -1, max_depth)
        turtle_.left(45)
    # правая версия
    else:
        turtle_.right(45)
        dragon_curve(length / 1.414, depth - 1, 1, max_depth)
        turtle_.left(90)
        dragon_curve(length / 1.414, depth - 1, -1, max_depth)
        turtle_.right(45)

# запускаем рисование
dragon_curve(600, 12, 1, 12)
screen.update()
turtle.done()
