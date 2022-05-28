import turtle


def go_forward():
    t.forward(10)


def go_backward():
    t.backward(10)


def turn_counterclockwise():
    t.setheading(t.heading() + 10)


def turn_clockwise():
    t.setheading(t.heading() - 10)


def clear():
    s.reset()


if __name__ == '__main__':
    s = turtle.getscreen()
    t = turtle.Turtle()
    t.speed(0)
    s.listen()
    s.onkey(go_forward, 'Up')
    s.onkey(go_backward, 'Down')
    s.onkey(turn_counterclockwise, 'Right')
    s.onkey(turn_clockwise, 'Left')
    s.onkey(clear, 'c')
    s.mainloop()
