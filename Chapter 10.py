import turtle
turtle.setup(400,500)

wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def advance_state_machine():

    global state_num

    if state_num == 0:
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine, 60)
    elif state_num == 1:
        tess.forward(70)
        tess.fillcolor("red")
        wn.ontimer(advance_state_machine, 1000)
        state_num = 2
    else:
        tess.back(140)
        tess.fillcolor("green")
        wn.ontimer(advance_state_machine, 1000)
        state_num = 0

def draw_housing():
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()
tess.penup()
tess.forward(40)
tess.left(90)
tess.forward(50)
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
state_num = 0

advance_state_machine()

wn.listen()

wn.mainloop()

import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess1 = turtle.Turtle()
tess2 = turtle.Turtle()

def draw_housing():

    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()

# Position tess onto the place where the green light should be

tess.forward(40)
tess.left(90)
tess.forward(50)
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
tess1.forward(40)
tess1.left(90)
tess1.forward(190)
tess1.shape("circle")
tess1.shapesize(3)
tess1.fillcolor("red")
tess2.forward(40)
tess2.left(90)
tess2.forward(120)
tess2.shape("circle")
tess2.shapesize(3)
tess2.fillcolor("orange")

state_num = 2

def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.fillcolor("black")
        tess1.fillcolor("black")
        tess2.fillcolor("orange")
        state_num = 1

    elif state_num == 1:
        tess.fillcolor("black")
        tess2.fillcolor("black")
        tess1.fillcolor("red")
        state_num = 2

    else:                    # Transition from state 2 to state 0
        tess1.fillcolor("black")
        tess2.fillcolor("black")
        tess.fillcolor("green")
        state_num = 0

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

wn.listen()                      # Listen for events
wn.mainloop()