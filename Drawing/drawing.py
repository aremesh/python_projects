import turtle


t = turtle.Turtle()


def square():
    """Drawing a square"""
    for i in range(4):
        turtle.forward(200)
        turtle.right(90)


def circle():
    """Drawing a circle"""
    t.circle(60)


def dot():
    """Setting a dot"""
    t.dot(30)


def loopCircle():
    """Loop a small circle"""
    n=1
    while n <= 4:
        t.circle(n)
        n = n+1


square()
dot()

# Keep the screen open until clicked
turtle.Screen().exitonclick()