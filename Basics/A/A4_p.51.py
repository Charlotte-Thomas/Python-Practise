
import turtle

#  ------- Turtle Graphics --------

# EXTRA:
# can mofiy the background, turtle image, pensize, turtle colour, filling in colours etc.


# | p.53 - 0.65 |

turtle.shape("turtle")
turtle.color('cyan', 'navy')

for i in range(0, 3):
    if i == 0:
        turtle.penup()
        turtle.backward(300)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(180)
        turtle.right(90)
    if i == 1:
        turtle.forward(180)
        turtle.right(90)
        turtle.forward(90)
        turtle.right(90)
        turtle.forward(180)
        turtle.left(90)
        turtle.forward(90)
        turtle.left(90)
        turtle.forward(180)
    if i == 2:
        turtle.forward(180)
        turtle.left(90)
        turtle.forward(90)
        turtle.left(90)
        turtle.forward(90)
        turtle.backward(90)
        turtle.right(90)
        turtle.forward(90)
        turtle.left(90)
        turtle.forward(180)

    turtle.penup()
    turtle.forward(90)
    turtle.pendown()

turtle.exitonclick()
