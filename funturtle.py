import turtle
finn = turtle.Turtle()
finn.shape('square')
finn.penup()
finn.goto(100,100)
finn.pendown()
finn.goto(200,100)
finn.goto(200,200)
finn.goto(100,200)
finn.goto(100,100)

charlie = turtle.Turtle()
charlie.shape('triangle')
charlie.goto(50,0)
charlie.stamp()
charlie.left(115)
charlie.forward(70)
charlie.stamp()
charlie.left(75)
charlie.forward(290)
charlie.stamp()
charlie.goto(50,0)

finn.goto(300,300)
finn.stamp()
finn.goto(100,100)

turtle.mainLoop()