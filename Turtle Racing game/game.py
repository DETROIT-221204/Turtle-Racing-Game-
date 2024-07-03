from turtle import Turtle, Screen
import random


screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your choice", prompt="Which turtle do you support? Enter a color: ")

colors = ["red", "orange", "pink", "green", "blue", "purple"]
turtles = []


for color in colors:
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    turtles.append(new_turtle)

spacing = 60
start_y = 150

for i, turtle in enumerate(turtles):
    turtle.goto(-200, start_y - i * spacing)
    turtle.pendown()


result_turtle = Turtle()
result_turtle.hideturtle()
result_turtle.penup()
result_turtle.goto(0, 0)
result_turtle.color("white")

is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle_speed = random.randint(0, 10)
        turtle.forward(turtle_speed)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            result_message = f"Winning turtle's color is {winning_color}. "

            if user_bet and user_bet.lower() == winning_color:
                result_message += "Congratulations! You win."
            else:
                result_message += f"Sorry, you bet on {user_bet} and the winner was {winning_color}." if user_bet else "No bet placed, please choose a turtle color next time."

            result_turtle.write(result_message, align="center", font=("Arial", 16, "normal"))

screen.exitonclick()
