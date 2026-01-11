import turtle                               # Подключаем библиотеку turtle для рисования

screen = turtle.Screen()
screen.bgcolor("white")

 
screen.tracer(1)                            #анимация пошаговая

turtle_ = turtle.Turtle()                   # Создаём объект "черепаха"
turtle_.color("green")
turtle_.speed(0)                            # Устанавливаем скорость рисования
turtle_.left(90)                            # Поворачиваем черепаху вверх (по умолчанию она смотрит вправо)
turtle_.penup()                             # Поднять перо, чтобы черепашка перемещалась без рисования. 
turtle_.goto(0, -250)                       # Перемещаем черепаху вниз экрана (точка начала дерева)
turtle_.pendown()                           # Опустить перо, чтобы черепашка начала рисовать линии при движении


def draw_tree(branch_length):
    # Условие остановки 
    if branch_length < 20:
        return

    turtle_.forward(branch_length)          # Рисуем текущую ветку вперёд на заданную длину

    turtle_.left(30)                        # Поворачиваем черепаху влево на 30 градусов
    draw_tree(branch_length - 20)           # Рекурсивно рисуем левую ветку, уменьшая длину

    turtle_.right(60)
    draw_tree(branch_length - 20)

    turtle_.left(30)                        # Возвращаем черепаху в исходное направление
    turtle_.backward(branch_length)         # Возвращаемся назад к началу текущей ветки

draw_tree(160)                              # Начальная длинна ветки 160

screen.update()                             # Обновляем экран и показываем результат рисования

turtle.done()
