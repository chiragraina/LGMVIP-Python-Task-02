import turtle
import time
import random
import winsound

# Initialize variables
initial_delay = 0.1
current_score = 0
max_score = 0

# Setup screen
screen = turtle.Screen()
screen.title("Classic Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize snake head
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("white")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

# Initialize snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.shape("square")
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Direction functions
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

def move_snake():
    if snake_head.direction == "up":
        snake_head.sety(snake_head.ycor() + 20)
    if snake_head.direction == "down":
        snake_head.sety(snake_head.ycor() - 20)
    if snake_head.direction == "left":
        snake_head.setx(snake_head.xcor() - 20)
    if snake_head.direction == "right":
        snake_head.setx(snake_head.xcor() + 20)

# Keyboard bindings
screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

# Function to start game
def initialize_game():
    global initial_delay, current_score
    initial_delay = 0.1
    current_score = 0
    snake_head.goto(0, 0)
    snake_head.direction = "stop"
    score_display.clear()
    score_display.write("Score: 0  High Score: {}".format(max_score), align="center", font=("Courier", 24, "normal"))

# Main game loop
while True:
    screen.update()

    # Check for border collision
    if abs(snake_head.xcor()) > 290 or abs(snake_head.ycor()) > 290:
        time.sleep(1)
        initialize_game()
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        initial_delay = 0.1

    # Check for food collision
    if snake_head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        initial_delay -= 0.001
        current_score += 10

        if current_score > max_score:
            max_score = current_score

        score_display.clear()
        score_display.write("Score: {}  High Score: {}".format(current_score, max_score), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("eat.wav", winsound.SND_ASYNC)

    # Move the snake segments in reverse order
    for idx in range(len(segments) - 1, 0, -1):
        x = segments[idx - 1].xcor()
        y = segments[idx - 1].ycor()
        segments[idx].goto(x, y)

    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)

    move_snake()

    # Check for collision with self
    for segment in segments:
        if segment.distance(snake_head) < 20:
            time.sleep(1)
            initialize_game()
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            initial_delay = 0.1
            score_display.clear()
            score_display.write("Score: {}  High Score: {}".format(current_score, max_score), align="center", font=("Courier", 24, "normal"))
            winsound.PlaySound("gameover.wav", winsound.SND_ASYNC)

    time.sleep(initial_delay)

screen.mainloop()
