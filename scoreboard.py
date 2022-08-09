from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-150,270)
        self.set_score()
    
    def set_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=("Arial",16,"normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER")

