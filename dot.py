
import random

color_list = [
    (153, 79, 35), (223, 155, 109), (109, 30, 42),
    (18, 52, 68), (57, 85, 99), (196, 199, 165),
    (102, 18, 27), (58, 85, 69), (216, 145, 4),
    (44, 77, 70), (213, 101, 53), (149, 32, 31),
    (9, 6, 5), (122, 68, 75), (187, 202, 175)
]

class Dot:
    
    def __init__(self,turtle):
        self.turtle = turtle
        
    def draw_dots(self,num_dots):
        
        for dot in range(num_dots):
        
            self.turtle.dot(20, random.choice(color_list))
            self.turtle.forward(50)
            
            if (dot + 1) % 10 == 0:
                self.turtle.setheading(90)
                self.turtle.forward(50) 
                self.turtle.setheading(180)  
                self.turtle.forward(50 * 10)  
                self.turtle.setheading(0)