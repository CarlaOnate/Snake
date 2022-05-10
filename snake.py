from turtle import *
from random import randrange
from wsgiref import headers
from freegames import square, vector

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
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
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
move()
triggerFood() # function to trigger moveFood function
done()