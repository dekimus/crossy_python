from turtle import Turtle

MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto(0,-280)
        self.shape("turtle")
        self.setheading(90)

    def move_up(self):
        self.setheading(90)
        newY = self.ycor() + MOVE_DISTANCE
        self.goto(0,newY)

    def move_down(self):
        if self.ycor() > -280:
            self.setheading(270)
            newY = self.ycor() - MOVE_DISTANCE
            self.goto(0,newY)