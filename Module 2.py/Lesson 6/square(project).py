import turtle


screen = turtle.Screen()
screen.bgcolor("lightblue")   


pen = turtle.Turtle()
pen.color("purple")
def draw_square():
    for i in range(4):
        pen.forward(100)
        pen.right(90)

draw_square()

turtle.done()
