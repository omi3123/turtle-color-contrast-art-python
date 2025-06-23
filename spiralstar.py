import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "green", "blue", "orange", "white"]
for i in range(150):
    t.pencolor(colors[i % 6])
    t.forward(i * 4)
    t.right(144)
turtle.done()