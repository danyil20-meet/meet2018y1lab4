import turtle
x = turtle.Turtle()
y = turtle.Turtle()
screen=turtle.Screen()

screen.bgcolor('purple')

x.pensize(5)
x.shape('circle')
x.color('white')
x.pencolor('yellow')

x.goto(0,150)
x.goto(-75, 150)
x.pencolor('white')
x.goto(-75, 0)

y.shape('triangle')
y.color('blue')
y.pencolor('green')
y.pensize(10)

y.goto(0,-150)
y.goto(75, -150)
y.pencolor('blue')
y.goto(75, 0)

turtle.mainLoop()
