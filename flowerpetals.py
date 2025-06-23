import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["magenta", "cyan", "yellow", "white"]
for i in range(36):
    t.pencolor(colors[i % 4])
    for j in range(2):
        t.circle(100, 60)
        t.left(120)
    t.right(10)
turtle.done()