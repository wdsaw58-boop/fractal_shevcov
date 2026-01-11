import turtle

screen = turtle.Screen()
screen.bgcolor("white")

screen.tracer(1)

turtle_ = turtle.Turtle()
turtle_.color("green")
turtle_.speed(10)
turtle_.hideturtle()   # скрываем черепаху (чтобы было красиво)

def koch_segment(length, depth):
    # условие остановки рекурсии
    if depth == 0:
        turtle_.forward(length)
        return

    # уменьшим длинну отрезка в 3 раза
    length /= 3

    # рекурсивно рисуем 4 сегмента
    # первая часть для кривой Коха
    koch_segment(length, depth - 1) 
    # поворачиваем на 60 градусов            
    turtle_.left(60)
    koch_segment(length, depth - 1)
    turtle_.right(120)
    koch_segment(length, depth - 1)
    turtle_.left(60)
    koch_segment(length, depth - 1)

def koch_snowflake(size, depth):
    # цикл выполним в 3 раза т.к у снежинки 3 части
    for _ in range(3):
        # рисуем одну сторону снежинки
        koch_segment(size, depth)
        # поворачиваем на следующую сторону 
        turtle_.right(120)

# перемещаем черепаху в начальную позицию
turtle_.penup()
turtle_.goto(-150, 100)
turtle_.pendown()

# рисуем снежинку
# 300 дланна стороны 
# 4 глубина рекурсии
koch_snowflake(300, 4) 

screen.update()

turtle.done()
