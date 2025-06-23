import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "blue", "green"]
for i in range(100):
    t.pencolor(colors[i % 4])
    t.forward(i * 3)
    t.left(91)
turtle.done()