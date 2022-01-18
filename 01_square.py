# Draw a square with Turtle
import turtle

s = 400
turtle.setup(width = 500, height = 500)

turtle.up()
turtle.goto(-200, -200)
turtle.down()

for i in range(0,4):

	turtle.forward(s)
	turtle.left(90)

turtle.done()
