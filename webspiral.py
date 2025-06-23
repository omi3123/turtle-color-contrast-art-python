import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["white", "cyan"]
for i in range(120):
    t.pencolor(colors[i % 2])
    t.forward(i * 2)
    t.left(60)
    t.forward(i)
    t.right(120)
turtle.done()