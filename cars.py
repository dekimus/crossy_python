from turtle import Turtle
import random
import turtle

velo = 5
INCREMENT = 10

class Car(Turtle):
    def __init__(self, in_play) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.color(self.gen_color())
        self.penup()
        self.velocity = velo
        self.in_play = in_play
        self.goto(self.starting_position(self.in_play))
        self.move()

    def starting_position(self, in_play):
        ypos = random.randint(-250, 300)
        xpos = random.randint(-250, 260)
        if in_play:
            return (275, ypos)
        else:
            return (xpos,ypos)

    def gen_color(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)

    def move(self):
        newX = self.xcor() - self.velocity
        self.goto(newX, self.ycor())
    
    def level_up(self):
        self.velocity += INCREMENT