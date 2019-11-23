#The Icelandic flag in all its glory 

import turtle 

def no_draw():
    turtle.speed(7)
    turtle.penup()
    turtle.right(180)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.pendown()

def text():
    turtle.color("dark red")
    style = ("Helvetica", 29, "bold","underline")
    turtle.write("The flag of Iceland in all its glory ", font = style, align='left')
    turtle.hideturtle()

def little_cross():
    turtle.color("black","red")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(160)

    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(130)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)

    turtle.forward(130)
    turtle.left(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(90)
    #turtle.left(90)
    turtle.end_fill()

    #moving the turtle a little bit forward so I can implement the text below the flag
    turtle.penup()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(170)
    text()



def square(x,y):
    no_draw()

    turtle.forward(x)
    turtle.right(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(y)
    turtle.right(90)
    
    

def topleft_square(x,y):
    turtle.color("black","blue")
    turtle.begin_fill()
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x-30)
    turtle.right(90)
    turtle.forward(x+350)
    turtle.right(90)
    turtle.end_fill()


def topright_square(x,y):
    turtle.color("black","blue")
    turtle.begin_fill()
    turtle.forward(y)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.end_fill()

def bottomright_square(x,y):
    turtle.color("black","blue")
    turtle.begin_fill()
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.forward(500)
    turtle.end_fill()
    
def bottomleft_square(x,y):
    turtle.color("black","blue")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(y)
    turtle.end_fill()
    little_cross()


square(500,250)
topleft_square(150,120)
topright_square(290,120)
bottomright_square(290,80)
bottomleft_square(150,80)

turtle.mainloop()
