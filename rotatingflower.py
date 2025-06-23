import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.pencolor("cyan")
for i in range(36):
    for j in range(2):
        t.circle(100, 60)
        t.left(120)
    t.right(10)
turtle.done()