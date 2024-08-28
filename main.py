
import turtle as ezgi
from dot import Dot

# Create a new turtle

ezgi.colormode(255)
ezgi.shape("turtle")
ezgi.color("DarkOliveGreen4")
ezgi.speed("fast")
ezgi.penup()
ezgi.hideturtle()
ezgi.goto(-100,-100)
number_of_dots = 100

new_dot = Dot(ezgi)
new_dot.draw_dots(number_of_dots)


# Set up the turtle screen and set the background color to white 

screen = ezgi.Screen() 
screen.bgcolor("white") 
screen.exitonclick()