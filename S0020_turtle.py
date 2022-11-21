"""
Exercise "Tom the Turtle":

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

The function "demo" introduces you to all commands you need to interact with Tom in the following exercises.

Only if you are curious and love details:
    Here is the full turtle graphics documentation:
    https://docs.python.org/3.3/library/turtle.html

Part 1:
    Write a function "square" which accepts a parameter "length".
    Calling this function causes the turtle to draw a square with a side length of "length" pixels.

Part 2:
     Write a function "visible" which returns a boolean value,
     indicating if the turtle is in the visible area of the screen.
     Use this function in the following parts of this exercise
     to return the turtle to the screen when it wandered off.

Part 3:
    Write a function "many_squares" with a for loop, which calls square repeatedly.
    Use this function to draw several squares of different sizes in different positions.
    The function shall have some parameters. For example:
        number: how many squares will be drawn?
        size: how large are the squares?
        distance: how far away from the last square is the next square positioned?

Part 4:
    Write a function that produces patterns similar to this:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Part 5:
    Write a function that produces patterns similar to this:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    The function shall have a parameter, that influences the shape of the pattern.

Part 6:
    Create your own function that produces a cool pattern.
    Later, if you like, present your pattern on the big screen to the others.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
import math

# def demo():  # demonstration of basic turtle commands
#     tom = turtle.Turtle()  # create an object named tom of type Turtle
#     print(type(tom))
#     tom.speed(1)  # fastest: 10, slowest: 1
#     for x in range(8):
#         tom.forward(100)  # move 100 pixels
#         tom.left(45)  # turn 45 degrees left
#         print("Tom is now at", tom.position())
#     tom.penup()  # do not draw while moving
#     tom.forward(222)
#     tom.pendown()  # draw while moving
#     tom.pencolor("red")  # draw in red
#     tom.right(90)  # turn 90 degrees right
#     tom.forward(333)
#     tom.home()  # return to the original position in the middle of the window
#     turtle.done()  # keeps the turtle window open after the program is done


def visible(turt):
    canvwidth, canvheight = turt.screen.screensize()
    if turt.xcor() < canvwidth and turt.ycor() < canvheight:
        return True
    else:
        return False


def base_square(length, tom):
    for i in range(4):
        tom.forward(length)
        tom.left(90)


def square(length, tom):
    tom.penup()
    lsquared = (length / 2) * (length / 2)
    c = math.sqrt(lsquared + lsquared)
    tom.right(135)
    tom.forward(c)
    tom.left(135)
    tom.pendown()
    base_square(length, tom)
    tom.penup()
    tom.speed(10)
    tom.left(45)
    tom.forward(c)
    tom.right(45)


def wanderoff():
    tom = turtle.Turtle()
    tom.speed(10)
    tom.forward(10000)
    print(visible(tom))
    turtle.done()


def many_squares(amount, length, distance):
    tom = turtle.Turtle()
    tom.speed(1)
    for i in range(amount):
        square(length[i], tom)
        tom.penup()
        tom.speed(10)
        tom.forward(length[i] / 2)
        tom.forward(distance)
        tom.forward(length[i + 1] / 2)
        tom.speed(1)
        tom.pendown()
    tom.penup()
    tom.home()
    turtle.done()


def math_many(amount, size, distance):
    squares = []
    for i in range(1, amount):
        squares.append(i * size)
    many_squares(amount, squares, distance)


def spiral():
    tom = turtle.Turtle()
    width, height = tom.screen.screensize()
    tom.speed(100)
    tom.penup()
    tom.setpos(-(width - 20), (height - 30))  # doesn't work
    tom.pendown()
    for i in range(1, 5):
        for x in range(int(width * 1.75 / 50)):
            base_square(50, tom)
            tom.forward(50)
        base_square(50, tom)
        tom.right(90)
        for y in range(int(height * 1.8 / 50)):
            base_square(50, tom)
            tom.forward(50)
        base_square(50, tom)
        tom.right(90)


# demo()
# square(100, turtle.Turtle())
# wanderoff()
# squares = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
# many_squares(len(squares), squares, 50)
# math_many(13, 10, 20)
spiral()
