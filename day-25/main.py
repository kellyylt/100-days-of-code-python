#Create a program to learn US States Names

import turtle
import pandas

game_is_on = True

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "100-days-of-code-python/day-25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_list = pandas.read_csv("100-days-of-code-python/day-25/50_states.csv")
guessed_state = []

while len(guessed_state) <= 50:

    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_list["state"].to_list():
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("100-days-of-code-python/day-25/states_to_learn.csv")
        break
        
    if answer_state in states_list["state"].to_list():
        x_cor = int(states_list[states_list["state"] == answer_state].x)
        y_cor = int(states_list[states_list["state"] == answer_state].y)
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cor, y_cor)
        t.write(answer_state)



