# @author: Kristin Dahl
# December 28, 2020
# Think Python, 2nd ed., Chapter 4

import turtle

def square(t, length=100):
    for i in range(4):
        t.fd(length)
        t.lt(90)

    turtle.mainloop()


def polygon(t, n=4, length=100):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

    turtle.mainloop()

def circle(t, r=4):
    circumference = 2 * 3.14159 * r
    length = circumference / 360
    polygon(t, 360, length)


def arc(t, r=4, angle=90):
    circumference = 2 * 3.14159 * r
    length = circumference / 360
    polygon(t, angle, length)


bob = turtle.Turtle()
#square(bob, 100)
#polygon(bob, 6, 100)
#circle(bob, 100)
arc(bob, 8, 90)