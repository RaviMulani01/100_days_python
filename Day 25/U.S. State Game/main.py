import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

# load image in turtle
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guess_state = []


while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 States Correct", prompt="What'another state's name?").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_state if state not in guess_state]
        print(missing_state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break


    if answer_state in all_state:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_info = data[data.state == answer_state]

        t.goto(int(state_info.x), int(state_info.y))
        t.write(state_info.state.item())


screen.exitonclick()



# get cordinate of screen when we click
# def get_mouse_click_cordinates(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_cordinates)

# not allow to exit on click when we click
# turtle.mainloop()