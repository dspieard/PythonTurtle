# Draw the
# Captain America Logo
# With Python Turtle

import turtle

r = 100
t = turtle.Turtle()
turtle.setup(width = 500, 
	height = 500)
turtle.bgcolor("#CDCDCD")
t.pen(pensize=10)

def draw_circle(c, p, r):
	t.begin_fill()
	t.color(c)
	t.penup()
	t.setposition(p)
	t.pendown()
	t.circle(r)
	t.end_fill()

def draw_star(c, p, f, r):
  t.begin_fill()
	t.color(c)
	t.penup()
	t.setposition(p)
	t.pendown()
	for i in range(5):
		t.forward(f)
		t.right(r)
	t.end_fill()

draw_circle("red", 
	(0, -r/2), r)
draw_circle("white", 
	(0, -r/2+15), r-15)
draw_circle("red", 
	(0, -r/2+30), r-30)
draw_circle("blue", 
	(0, -r/2+45), r-45)
draw_star("white",
	(-50,68), 100, 144)
draw_circle("white", 
	(0, 30), 20)

turtle.done()
