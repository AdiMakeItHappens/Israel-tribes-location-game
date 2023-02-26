import turtle
import pandas

turtle.screensize(514, 941, bg="light blue")
screen = turtle.Screen()
screen.title("Israel map Game")
screen.setup(width=0.9, height=0.9)

# image is gif because Turtle can read images just in this way
image = "Israel_relief_location_map.gif"

# to add backround image
screen.addshape(image)
turtle.shape(image)

# collect the data from csv file
data_tribes = pandas.read_csv("tribes_name.csv")
# collecting from data all the states and converting them to list
all_tribes = data_tribes.tribe.to_list()


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# # that's will listen when the mouse clicks and it will call our get_mouse_click_coor and pass over x and y coordinate
# turtle.onscreenclick(get_mouse_click_coor)

guessed_tribes = []

while len(guessed_tribes) < 12:
    answer_tribe = screen.textinput(title=f"{len(guessed_tribes)}/12 tribes Correct",
                                    prompt="What's another tribes name?").title()

    # if the user wrote exit it will end the game and save the results in csv file
    if answer_tribe == "Exit":
        missing_tribes= []
        for tribe in all_tribes:
            if tribe not in guessed_tribes:
                missing_tribes.append(tribe)
        new_data = pandas.DataFrame(missing_tribes)
        new_data.to_csv("tribes_to_learn.csv")
        break

    # If answer_state is one of the states in all states of the 50_states.csv
    if answer_tribe in all_tribes:
        guessed_tribes.append(answer_tribe)
        # If they got it right:
        # Create a Turtle to write the name of the state at the state's x and y coordnate
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # if data.state equal to answer_state
        # write the name of the state at the state's x and y coordnate
        tribe_data = data_tribes[data_tribes.tribe == answer_tribe]
        t.goto(int(tribe_data.x), int(tribe_data.y))
        t.write(tribe_data.tribe.item())


# screen.mainloop()
