import turtle as t
import colorsys

window = t.Screen()
window.setup(width = 1.0, height = 1.0)
canvas = window.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

t.tracer(10)
t.pensize(2)
t.setpos(-40, 30)
h = 0.5
t.bgcolor('black')

for i in range(800):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    h+= 0.004
    t.fd(i)
    t.rt(31)
    t.fd(i)
    t.rt(150)



# Defining a method to draw curve
def drawcurve():
    for i in range(800):
        # Defining step by step curve motion
        vr.right(1)
        vr. forward(1)

# Creating a turtle object(vr)
vr = t.Turtle()
# set the pen size
t.pensize(4)
vr.speed (10)
vr.penup()
vr.setpos(-40,-50)
vr.pendown()

# Defining a method to draw curve
def drawcurve():
    for i in range(200):
        # Defining step by step curve motion
        vr.right(1)
        vr. forward(1)
        


# Set the fill color to pink and border color to Red
vr.color('red', 'pink')
 # Start filling the color
vr.begin_fill()
vr.left(140)

 # Draw the left line
vr.forward(111.65)
# Draw the left curve
drawcurve()
vr.left(120)
drawcurve()
 # Draw the right line
vr.forward(111.65)
 # end_fill() : This method fills the polygon with the current fill color by closing it between the current position and the initial position.
vr.end_fill()
vr.penup()
vr.goto(77, -40)
vr.pendown()
vr.hideturtle()

t.penup()
t.setpos(-225,0)
t.pendown()
t.pencolor('black')
t.write("Marry Me?", font=("Verdana",
                                    64, "normal"))
t.exitonclick()
