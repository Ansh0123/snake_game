import time
import turtle
import random

# variables
score = 0
max_score = 0
delay = 0.1

s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600, height=600)
s.tracer(0)

snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("white")
snake_head.fillcolor("blue")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"
# bodies.append(snake_head)

# food
snake_food = turtle.Turtle()
snake_food.speed(0)
snake_food.shape("circle")
snake_food.color("yellow")
snake_food.fillcolor("green")
snake_food.penup()
snake_food.ht()
snake_food.goto(0, 200)
snake_food.st()

score_board = turtle.Turtle()
score_board.shape("square")
score_board.fillcolor("black")
score_board.penup()
score_board.ht()
score_board.goto(-270, 280)
score_board.write("score : 0 | Max Score : 0")

def move_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def move_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def move_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def move_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

def pause():
    snake_head.direction = "stop"

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)

s.listen()
s.onkey(move_up, "Up")
s.onkey(move_down, "Down")
s.onkey(move_left, "Left")
s.onkey(move_right, "Right")
s.onkey(pause, "space")

bodies = []

while True:
    s.update()
    if snake_head.xcor() > 290:
        snake_head.setx(-290)
    if snake_head.xcor() < -290:
        snake_head.setx(290)
    if snake_head.ycor() > 290:
        snake_head.sety(-290)
    if snake_head.ycor() < -290:
        snake_head.sety(290)

    if snake_head.distance(snake_food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        snake_food.goto(x, y)
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)

        score += 10
        delay -= 0.001
        if score > max_score:
            max_score = score

        score_board.clear()
        score_board.write("Score : {} Max Score {}".format(score, max_score))

    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        bodies[0].goto(x, y)

    move()

    for body in bodies:
        if body.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"

            for bd in bodies:
                bd.ht()
            bodies.clear()
            score = 0
            delay = 0.1
            score_board.clear()
            score_board.write("Score : {} Max Score {}".format(0, max_score))

    time.sleep(delay)

# s.mainloop()
