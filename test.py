import turtle                            #importing the turtle module

t = turtle.Turtle()                            #create the turtle t
wn = turtle.Screen()                            #draw the canvas for turtle
turtle.bgcolor("grey")                            #make the background colour grey
t.speed(300)                            #increase the turtle speed to 300
t.pensize(2)                            #choose the pesize of two
t.pu()                            #pen up the turtle
t.hideturtle()                            #hide the turtle 
box_color = True                            #intialize boolean variable for box colour change

def main():
    RingDirection = False                            #
    for i in range(5):
        if(RingDirection==False):
            circleAntiClock(18*(i+1), i+1)
            RingDirection = True
        elif(RingDirection==True):
            circleClockwise(18*(i+1), i+1)
            RingDirection = False
    wn.exitonclick()
#------------------------------------------------------------------------            
def CirclePosition(p):
    t.goto(0, -(60*p))
#------------------------------------------------------------------------        
def circleAntiClock(p, s):
    for i in range(p):
        square(s)
        t.forward(24)
        t.left(360/p)        
    CirclePosition(s)
#------------------------------------------------------------------------    
def circleClockwise(p, s):
    for i in range(p):
        square(s)
        t.forward(24)
        t.left(360/p)
    CirclePosition(s)

#------------------------------------------------------------------------        
def square(s):
    t.pd()
    if(s%2==0):
        t.left(15)
    else:
        t.left(-15)
        
    global box_color 
    if(box_color==True):
        t.color("white")
        box_color=False
    else:
        t.color("black")
        box_color=True
        
    for i in range(4):
        t.forward(20)
        t.left(90)
    if(s%2==0):
        t.left(-15)
    else:
        t.left(15)
    t.pu()
#------------------------------------------------------------------------    
if(__name__=="__main__"):
    main()
