from turtle import *
from random import randrange
from wsgiref import headers
from freegames import square, vector

# Octavio Augusto Alemán A01660702
# Carla Oñate Gardella A01653555

food = vector(100, 100)
snake = [vector(10, 0)]
aim = vector(0, -10)

def moveFood():
    head = snake[-1].copy() # Find snake position
    axis = randrange(0, 2) # To change position in the x axis or y axis
    direction = randrange(0, 3) # To add or subtract from position
    if not food == head and inside(food):
        if axis == 0: # if axis 0 then change x axis
            if direction == 0:
                food.x += 10 # if direction 0 then sum
            else:
                food.x -= 10 # if direction 0 then subtract
        elif axis == 1: # if axis 1 then change y axis
            if direction == 0:
                food.y += 10
            else:
                food.y -= 10
    elif not inside(food):
        food.x = 0 # if not inside then go to start position
        food.y = 0

def triggerFood(): # recursive loop to change food every 500 milliseconds
    moveFood() # call move food
    update() # update canvas
    ontimer(triggerFood, 500) # create timer to call again triggerFood to move the food again

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# randomColor() function has been added. Its purpose is to choose from a list containing 7 different colors, one random color for the snake and one random color for the target, also considering that those two colors have to be different. 

def randomColor():
    colors = ['black', 'green', 'purple', 'orange', 'yellow', 'blue', 'pink'] #The list containing the colors is created.

    x = randrange(1, 7, 1) #A random number between 1 and 7 is chosen. 

    global colorSnake # The global variable colorSnake is defined.
    colorSnake = colors[x] # A value is asigned to the colorSnake variable. The color is chosen based on the previously generated random number, taking the color from that index in the colors[] list. 
    colors.pop(x) #The first used color is taken out from the list, so that it isn't repeated.

    x = randrange(1, 6, 1) #A second random number between 1 and 6 is chosen.
    global colorSquare # The global variable colorSquare is defined.
    colorSquare = colors[x] # A value is asigned to the colorSquare variable.

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSnake) # The color based on the colorSnake variable is asigned.

    square(food.x, food.y, 9, colorSquare) # The color based on the colorSquare variable is asigned.
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
randomColor() # The function is called so that it asigns values to the global variables colorSnake and colorSquare.
move()
triggerFood() # function to trigger moveFood function
done()