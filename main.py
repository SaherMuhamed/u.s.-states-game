import pandas
from turtle import Turtle, Screen

FONT = ("Courier", 8, "bold")

# TODO: Make objects from turtle class.
screen = Screen()

# TODO: Setting up the screen game.
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
screen.title("U.S. States Game")

# TODO: Open the csv file and read it.
states_file = pandas.read_csv("50_states.csv")

# TODO: Convert states file to list to easily loop on it.
states_list = states_file["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 of States",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("remaining_states.csv")
        break

    if answer_state == states_list:
        guessed_states.append(answer_state)
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = states_file[states_file.state == answer_state]
        new_turtle.goto(x=int(state_data.x), y=int(state_data.y))
        new_turtle.write(arg=answer_state, font=FONT)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen.exitonclick()
