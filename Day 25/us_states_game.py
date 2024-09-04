import pandas as pd
import turtle

# Setting up the screen and turtle shape as a custom image
screen = turtle.Screen()
screen.title("U. S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reading the CSV
data = pd.read_csv("50_states.csv")

# Game logic
correct_answers = []
game_is_on = True
while game_is_on:

    # Setting up conditional statement to change the user input box title
    if len(correct_answers) == 0:
        answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
        answer_state = answer_state.title()
    else:
        answer_state = screen.textinput(title=f"{len(correct_answers)}/50 states correct", prompt="What's another state's name")
        answer_state = answer_state.title()

    # Checking user answer
    if answer_state in correct_answers:
        continue
    elif answer_state in data["state"].values:
        name_on_map = turtle.Turtle()
        name_on_map.hideturtle()
        name_on_map.penup()
        get_answer = data[data["state"] == answer_state]
        name_on_map.teleport(x=data.iloc[get_answer.index.item()]["x"], y=data.iloc[get_answer.index.item()]["y"])
        name_on_map.write(answer_state, align="center")
        correct_answers.append(answer_state)
    elif answer_state == "Exit":
        with open("states_to_learn.csv", mode="w") as file:
            for state in data["state"].values:
                if state not in correct_answers:
                    file.write(f"{state}\n")
        game_is_on = False

    # Game over sequence
    if len(correct_answers) == 50:
        game_is_on = False
        name_on_map.clear()
        game_over = turtle.Turtle()
        game_over.hideturtle()
        game_over.write("YOU WIN!", align="center", font=("Arial", 50, "bold"))