# imports
import turtle
import math

# globals
xSize = 600
ySize = 600
wn   = turtle.Screen()
turt = turtle.Turtle()
turt.hideturtle()



# draw X
def drawX():
    diagonal = ((200**2)+(200**2))**(1/2)                  #calculate distance accross block
    turt.right(45)
    turt.forward(diagonal)
    turt.right(135)                                             #.....draw the 
    turt.forward(200)                                            #X using turtle
    turt.right(135)
    turt.forward(diagonal)
    turt.right(45)
    turt.forward(-200)



# is the co-ord on the board?
def onBoard(qX, qY):
    if(qX >= -300 and qX <= 300 and qY >= -300 and qY <= 300):        #check if click is within box
        return True    
    else:
        return False

# return which quadrant was clicked in
#
# +-----+-----+-----+
# |     |     |     |
# | 2,0 | 2,1 | 2,2 |
# |     |     |     |
# +-----+-----+-----+
# |     |     |     |
# | 1,0 | 1,1 | 1,2 |
# |     |     |     |
# +-----+-----+-----+
# |     |     |     |
# | 0,0 | 0,1 | 0,2 |
# |     |     |     |
# +-----+-----+-----+
#
def quadrant(x, y):                          #fuction to move to clicked quadrant
    xBlockSize = xSize/3
    yBlockSize = ySize/3
    
    if(x>-300 and x<-100 and y>-300 and y<-100):         #bottom left
        xc = 1
        yc = 1
    elif(x>-100 and x<100 and y>-300 and y<-100):         #bottom center
        xc = 2
        yc = 1
    elif(x>100 and x<300 and y>-300 and y<-100):         #bottom right
        xc = 3
        yc = 1
    elif(x>-300 and x<-100 and y>-100 and y<100):         #center left
        xc = 1
        yc = 2
    elif(x>-100 and x<100 and y>-100 and y<100):         #center center
        xc = 2
        yc = 2
    elif(x>100 and x<300 and y>-100 and y<100):         #center right
        xc = 3
        yc = 2
    elif(x>-300 and x<-100 and y>100 and y<300):         #top left
        xc = 1
        yc = 3
    elif(x>-100 and x<100 and y>100 and y<300):         #top center
        xc = 2
        yc = 3
    elif(x>100 and x<300 and y>100 and y<300):         #top right
        xc = 3
        yc = 3
    
    
    
    # 3 rows and 3 columns
    for i in range(xc):                               #....using two for loops to
        for j in range(yc):                             #the clicked quadrant
            turt.penup()
            turt.goto(i*xBlockSize - (xSize/2), j*yBlockSize - (ySize/2)+(yBlockSize))
            turt.pendown()
    drawX()
    



# when we click on the turtle window we call this function
# when the click occurs, the X and Y co-ord of where we clicked is passed in as the x and y paramaters
def boardClick(x, y):
    print("Click Co-Ords")
    print("X: " + str(x))
    print("Y: " + str(y))
    if(onBoard(x, y)==True):                    #.....if within one of the quadrants
        quadrant(x, y)                        #call function to move turtle to it



def drawSquare(xSz, ySz):
    turt.forward(xSz)
    turt.right(90)
    turt.forward(ySz)
    turt.right(90)
    turt.forward(xSz)
    turt.right(90)
    turt.forward(ySz)
    turt.right(90)
    


# draw starting board
def drawBoard():
    xBlockSize = xSize/3
    yBlockSize = ySize/3

    # 3 rows and 3 columns
    for i in range(3):
        for j in range(3):
            turt.penup()
            turt.goto(i*xBlockSize - (xSize/2), j*yBlockSize - (ySize/2)+(yBlockSize))     # draw centered
            turt.pendown()
            drawSquare(xBlockSize, yBlockSize)



# that main method boy!
def main():
    turt.speed(100)
    
    drawBoard()
    wn.onclick(boardClick)  # create callback

    turtle.mainloop()       # enter into mainloop and wait for click events



# if we are the one being called, call main :D
if __name__ == "__main__":
    main()


