######################################################################
#Username: Martinj2
# Assignment: A02: Loopy Turtles
######################################################################



import turtle


wn = turtle.Screen()

ne = turtle.Turtle()
turtle = turtle.Turtle()
wn.bgcolor("purple")





ne.pendown
ne.forward(90)
for q in range(8):
     ne.forward(25)
     ne.right(20)
     ne.left(65)
     ne.forward(-90)

turtle.penup
turtle.left(180)
turtle.forward(15)
turtle.pendown
"""Move the starting position of the pen, so that is centered further to the right on the screen"""



def a_function():
    for z in range(5):
        turtle.color("red")
        turtle.forward(25)
        turtle.right(30)
###"""Makes a loop function that makes a circle and moves it the right 30 degrees"""


def my_function():
    for i in range(15):
        turtle.pendown
        turtle.forward(10)
        turtle.left(30)
        turtle.penup
#Makes a loop function that creates the circles


for s in range(7):
    turtle.pendown
    turtle.forward(20)
    my_function()
    a_function()
    turtle.penup
#Makes a loop that call both functions into the loop.


tList = []                                          ###Makes an empty list
tList.append(turtle)                                ###adds turtle to list
w = tList[0]                                        ###gives the list a range of 0

w.up()

w.setpos(-100,-100)
w.write("Abstract Art brings a smile to my face.")

###Writes I love loops, to indicate something that makes me happy.


wn.exitonclick()