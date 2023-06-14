from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(1024, 512)
screen.title("TURTLE RACE")

choice = screen.textinput("UserIn", "Choose your turtle(blue, red, green, yellow, purple, black): ")

Screen().bgpic("giphy.gif")

textHead = Turtle()
textHead.penup()
textHead.hideturtle()
textHead.setposition(0, 190)
textHead.fillcolor("gray")
textHead.write("TURTLE RACE", font=("Arial", 40, "bold"), align="center")

screen.tracer(0)
#finish line
line = Turtle()

line.width(1)
line.penup()
line.setx(400+15)
line.pendown()
line.sety(300)
line.sety(-300)


colors = ["blue", "red", "green", "yellow", "purple", "black"]

turtle_all = []
for i in range(6):

    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape('turtle')

    turtle_all.append(new_turtle)
    turtle_all[i].fillcolor(colors[i])
    # turtle_all[i].setx(-500)
    # turtle_all[i].sety(-200+(i*50))
    turtle_all[i].setposition(-500, -200+(i*50))

screen.tracer(1)

race_on = True

while race_on:

    for turtle in turtle_all:

        if turtle.xcor() >= 400:
            whichTurtle = turtle_all.index(turtle)
            race_on = False
            break

        rand_dis = random.randint(1, 10)

        if turtle.xcor() + rand_dis < 400:
            turtle.forward(rand_dis)

        elif turtle.xcor() + rand_dis >= 400:
            turtle.forward(400 - turtle.xcor())

        if turtle.xcor() >= 400:
            whichTurtle = turtle_all.index(turtle)
            race_on = False
            break


    # if turtle.xcor() == 400:
    #     race_on = False
print(f"Your {choice} turtle result.")
print(f"{colors[whichTurtle]} turtle is the winner!")

screen.exitonclick()
