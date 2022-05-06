import turtle
#function
#loop and for the three sides
def drawTriangle(triangle, triangleside): 
    for _ in range(3): 
        triangle.forward(triangleside)
        triangle.left(120)
        triangle.forward(triangleside)
# Forward turtle by sides units
    for _ in range(4):
        triangle.forward(triangleside) 
        triangle.left(90)


triangle= turtle.Turtle()
drawTriangle(triangle, 100)
