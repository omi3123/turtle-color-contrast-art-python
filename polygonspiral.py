import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
for i in range(180):
    t.pencolor(colors[i % 6])
    t.forward(i)
    t.left(91)
turtle.done()