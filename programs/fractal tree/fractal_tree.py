from turtle import *
speed(0)


def draw(size, levels, angle):
    if levels == 0:
        color("green")
        dot(size)
        color("black")
        return

    forward(size)
    right(angle)

    draw(size * 0.67, levels - 1, angle)

    left(angle * 2)

    draw(size * 0.67, levels - 1, angle)
    right(angle)
    back(size)


left(90)
draw(100, 7, 45)

mainloop()
