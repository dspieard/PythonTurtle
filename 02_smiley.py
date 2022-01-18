# Turtle, Blue Monday? Keep Smiling :)
import turtle

r = 100
t = turtle.Turtle()
turtle.setup(
	width = 500,
	height = 500
	)
t.pen(
	fillcolor=('#0080FF'),
	pensize=10
	)

t.up()
t.goto(0, -100)
t.down()

t.begin_fill()
t.circle(r)
t.end_fill()

t.fillcolor('black')

t.begin_fill()
t.up()
t.goto(-45, 20)
t.down()
t.circle(r/6)
t.end_fill()

t.begin_fill()
t.up()
t.goto(45, 20)
t.down()
t.circle(r/6)
t.end_fill()

t.up()
t.goto(-45, -30)
t.down()
t.right(90)
t.circle(50,180)

turtle.done()
