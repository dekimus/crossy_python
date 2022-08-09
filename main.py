import time
from turtle import Screen
from player import Player
from cars import Car
from scoreboard import ScoreBoard



sc = Screen()
sc.colormode(255)
sc.setup(600, 600)
sc.title("Crossy pacos")
sc.tracer(0)
sc.update()
sc.listen()
cars = []
player = Player()
sb = ScoreBoard()
sc.onkeypress(fun=player.move_up, key="w")
sc.onkeypress(fun=player.move_down, key="s")

for i in range(15):
    car = Car(False)
    cars.append(car)
on_play = True


while on_play:
    time.sleep(0.06)
    sc.update()

    for c in cars:
        c.move()
        if player.distance(c) < 25:
            on_play = False
            sb.game_over()
        if c.xcor() < -290:
            c.goto(c.starting_position(True))
    
    if player.ycor() > 280:
        sb.set_score()
        player.goto(0, -270)
        for c in cars:
            c.level_up()



    
    

    











sc.exitonclick()