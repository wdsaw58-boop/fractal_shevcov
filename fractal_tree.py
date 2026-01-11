import turtle

screen = turtle.Screen()
screen.bgcolor("white")

#анимация
screen.tracer(1)

t = turtle.Turtle()
t.color("green")
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()


def draw_tree(branch_length):
    # Условие остановки 
    if branch_length < 20:
        return

    t.forward(branch_length)

    t.left(30)
    draw_tree(branch_length - 20)

    t.right(60)
    draw_tree(branch_length - 20)

    t.left(30)
    t.backward(branch_length)

draw_tree(100)

screen.update()

turtle.done()
