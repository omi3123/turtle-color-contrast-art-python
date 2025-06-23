import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["#00ffff", "#ff00ff", "#ffff00"]
for i in range(72):
    t.pencolor(colors[i % 3])
    t.circle(100)
    t.left(5)
turtle.done()