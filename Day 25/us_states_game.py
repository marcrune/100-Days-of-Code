import pandas as pd
import turtle

# Setting up the screen and turtle shape as a custom image
screen = turtle.Screen()
screen.title("U. S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
print(data.iloc[34]["x"])
print(data.iloc[data[data["state"] == "Ohio"].index.item()]["x"])

# Getting the user input and capitalizing it
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
    answer_state = answer_state.capitalize()

    # Reading the CSV using pandas
    data = pd.read_csv("50_states.csv")
    if answer_state in data["state"]:
        name_on_map = turtle.Turtle()
        name_on_map.fillcolor("black")
        get_answer = data[data["state"] == answer_state]
        name_on_map.teleport(x=data.iloc[get_answer.index.item()]["x"], y=data.iloc[get_answer.index.item()]["y"])
        name_on_map.write(answer_state)



# screen.exitonclick()