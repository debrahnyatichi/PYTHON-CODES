import turtle

t=turtle.Turtle()
s=turtle.Turtle()

t.hideturtle()
t.goto(0,-10)

t.pensize(3)
t.color('Purple')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()

t.goto(-130,130)
t.pendown()
t.color('white')
t.write("Hey Love! \n Do you know you are the most Special \n Person in My life?\n I love you so much\n I will always treasure you \n",font=("Verdana",8,"bold"))
turtle.done()
