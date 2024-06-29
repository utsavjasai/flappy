# import turtle
# import time

# # Register the bird image as a shape
# turtle.register_shape("bird.gif")

# # Set up the screen
# wn = turtle.Screen()
# wn.title("Flappy Bird")
# wn.bgcolor("blue")
# wn.bgpic("background.gif")
# wn.setup(width=375, height=667)  # Typical mobile phone screen size
# wn.tracer(0)

# # Set up the pen for score display
# pen = turtle.Turtle()
# pen.speed(0)
# pen.hideturtle()
# pen.penup()
# pen.color("white")
# pen.goto(0, 250)
# pen.write("0", move=False, align="left", font=("Arial", 32, "normal"))

# # Set up the player
# player = turtle.Turtle()
# player.speed(0)
# player.penup()
# player.color("yellow")
# player.shape("bird.gif")  # Set the player shape to the registered image
# player.goto(-200, 0)
# player.dx = 0
# player.dy = 1

# # Set up the pipes
# def create_pipe(x, y):
#     pipe = turtle.Turtle()
#     pipe.speed(0)
#     pipe.penup()
#     pipe.color("green")
#     pipe.shape("square")
#     pipe.shapesize(stretch_wid=18, stretch_len=3, outline=None)
#     pipe.goto(x, y)
#     pipe.dx = -2
#     pipe.dy = 0
#     return pipe

# pipe1_top = create_pipe(300, 250)
# pipe1_bottom = create_pipe(300, -250)
# pipe2_top = create_pipe(600, 300)
# pipe2_bottom = create_pipe(600, -200)

# gravity = -0.3

# # Define function / method to move the player up
# def go_up(x, y):
#     player.dy += 8
#     if player.dy > 8:
#         player.dy = 8

# # Bind the screen click to the go_up function
# wn.onscreenclick(go_up)

# # Initialize game variables
# player.score = 0
# highest_score = 0  # Initialize highest score

# # Main Game Loop
# while True:
#     # Pause
#     time.sleep(0.01)
#     # Update the screen
#     wn.update()
    
#     # Add gravity
#     player.dy += gravity
    
#     # Move player
#     y = player.ycor()
#     y += player.dy
#     player.sety(y)
    
#     # Bottom Border
#     if player.ycor() < -325:
#         player.dy = 0
#         player.sety(-325)

#     # Move Pipe 1
#     x = pipe1_top.xcor()
#     x += pipe1_top.dx
#     pipe1_top.setx(x) 
    
#     x = pipe1_bottom.xcor()
#     x += pipe1_bottom.dx
#     pipe1_bottom.setx(x)
    
#     # Return pipes to start
#     if pipe1_top.xcor() < -200:
#         pipe1_top.setx(375)
#         pipe1_bottom.setx(375)
#         pipe1_top.value = 1

#     # Move Pipe 2
#     x = pipe2_top.xcor()
#     x += pipe2_top.dx
#     pipe2_top.setx(x) 
    
#     x = pipe2_bottom.xcor()
#     x += pipe2_bottom.dx
#     pipe2_bottom.setx(x)
    
#     # Return pipes to start
#     if pipe2_top.xcor() < -200:
#         pipe2_top.setx(375)
#         pipe2_bottom.setx(375)
#         pipe2_top.value = 1

#     # Check for collisions with pipes
#     # Pipe 1
#     if (player.xcor() + 10 > pipe1_top.xcor() - 30) and (player.xcor() - 10 < pipe1_top.xcor() + 30):
#         if (player.ycor() + 10 > pipe1_top.ycor() - 180) or (player.ycor() - 10 < pipe1_bottom.ycor() + 180):
#             pen.clear()
#             pen.write("Game Over", move=False, align="center", font=("Arial", 16, "normal"))
#             wn.update()
#             time.sleep(3)
#             # Reset score
#             player.score = 0
#             # Move Pipes Back
#             pipe1_top.setx(300)
#             pipe1_bottom.setx(300)
#             pipe1_top.setx(600)
#             pipe1_bottom.setx(600)
#             # Move Player back
#             player.goto(-200, 0)
#             player.dy = 0
            
#     # Check for score        
#     if pipe1_top.xcor() + 30 < player.xcor() - 10:
#         player.score += pipe1_top.value
#         pipe1_top.value = 0
#         # Update highest score if needed
#         if player.score > highest_score:
#             highest_score = player.score
#         # Update score display
#         pen.clear()
#         pen.write(f"Score: {player.score}  Highest: {highest_score}", move=False, align="center", font=("Arial", 32, "normal"))

#     # Check for collisions with pipes
#     # Pipe 2
#     if (player.xcor() + 10 > pipe2_top.xcor() - 30) and (player.xcor() - 10 < pipe2_top.xcor() + 30):
#         if (player.ycor() + 10 > pipe2_top.ycor() - 180) or (player.ycor() - 30 < pipe2_bottom.ycor() + 180):
#             pen.clear()
#             pen.write("Game Over", move=False, align="left", font=("Arial", 16, "normal"))
#             wn.update()
#             time.sleep(3)
#             # Reset score
#             player.score = 0
#             # Move Pipes Back
#             pipe2_top.setx(300)
#             pipe2_bottom.setx(300)
#             pipe2_top.setx(600)
#             pipe2_bottom.setx(600)
#             # Move Player back
#             player.goto(-200, 0)
#             player.dy = 0
#             # Clear the pen
#             pen.clear()
            
#     # Check for score        
#     if pipe2_top.xcor() + 30 < player.xcor() - 10:
#         player.score += pipe2_top.value
#         pipe2_top.value = 0
#         # Update highest score if needed
#         if player.score > highest_score:
#             highest_score = player.score
#         # Update score display
#         pen.clear()
#         pen.write(f"Score: {player.score}  Highest: {highest_score}", move=False, align="center", font=("Arial", 32, "normal"))

# wn.mainloop()

import turtle
import time

# Register the bird image as a shape
turtle.register_shape("bird.gif")

# Set up the screen
wn = turtle.Screen()
wn.title("Flappy Bird")
wn.bgcolor("blue")
wn.bgpic("background.gif")
wn.setup(width=375, height=667)  # Typical mobile phone screen size
wn.tracer(0)

# Set up the pen for score display
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 250)
pen.write("0", move=False, align="left", font=("Arial", 32, "normal"))

# Set up the player
player = turtle.Turtle()
player.speed(0)
player.penup()
player.color("yellow")
player.shape("bird.gif")  # Set the player shape to the registered image
player.goto(-200, 0)
player.dx = 0
player.dy = 1

# Set up the pipes
def create_pipe(x, y):
    pipe = turtle.Turtle()
    pipe.speed(0)
    pipe.penup()
    pipe.color("green")
    pipe.shape("square")
    pipe.shapesize(stretch_wid=18, stretch_len=3, outline=None)
    pipe.goto(x, y)
    pipe.dx = -2
    pipe.dy = 0
    return pipe

pipe1_top = create_pipe(300, 250)
pipe1_bottom = create_pipe(300, -250)
pipe2_top = create_pipe(600, 300)
pipe2_bottom = create_pipe(600, -200)

gravity = -0.3

# Define function / method to move the player up
def go_up(x, y):
    player.dy += 8
    if player.dy > 8:
        player.dy = 8

# Bind the screen click to the go_up function
wn.onscreenclick(go_up)

# Initialize game variables
player.score = 0
highest_score = 0  # Initialize highest score

# Main Game Loop
while True:
    # Pause
    time.sleep(0.01)
    # Update the screen
    wn.update()
    
    # Add gravity
    player.dy += gravity
    
    # Move player
    y = player.ycor()
    y += player.dy
    player.sety(y)
    
    # Bottom Border
    if player.ycor() < -325:
        player.dy = 0
        player.sety(-325)

    # Move Pipe 1
    x = pipe1_top.xcor()
    x += pipe1_top.dx
    pipe1_top.setx(x) 
    
    x = pipe1_bottom.xcor()
    x += pipe1_bottom.dx
    pipe1_bottom.setx(x)
    
    # Return pipes to start
    if pipe1_top.xcor() < -200:
        pipe1_top.setx(375)
        pipe1_bottom.setx(375)
        pipe1_top.value = 1

    # Move Pipe 2
    x = pipe2_top.xcor()
    x += pipe2_top.dx
    pipe2_top.setx(x) 
    
    x = pipe2_bottom.xcor()
    x += pipe2_bottom.dx
    pipe2_bottom.setx(x)
    
    # Return pipes to start
    if pipe2_top.xcor() < -200:
        pipe2_top.setx(375)
        pipe2_bottom.setx(375)
        pipe2_top.value = 1

    # Check for collisions with pipes
    # Pipe 1
    if (player.xcor() + 10 > pipe1_top.xcor() - 30) and (player.xcor() - 10 < pipe1_top.xcor() + 30):
        if (player.ycor() + 10 > pipe1_top.ycor() - 180) or (player.ycor() - 10 < pipe1_bottom.ycor() + 180):
            pen.clear()
            pen.write("Game Over", move=False, align="center", font=("Arial", 16, "normal"))
            wn.update()
            time.sleep(3)
            # Reset score
            player.score = 0
            # Move Pipes Back
            pipe1_top.setx(300)
            pipe1_bottom.setx(300)
            pipe1_top.setx(600)
            pipe1_bottom.setx(600)
            # Move Player back
            player.goto(-200, 0)
            player.dy = 0
            
    # Check for score        
    if pipe1_top.xcor() + 30 < player.xcor() - 10:
        player.score += pipe1_top.value
        pipe1_top.value = 0
        # Update highest score if needed
        if player.score > highest_score:
            highest_score = player.score
        # Update score display
        pen.clear()
        pen.write(f"Score: {player.score}  Highest: {highest_score}", move=False, align="center", font=("Arial", 32, "normal"))

    # Check for collisions with pipes
    # Pipe 2
    if (player.xcor() + 10 > pipe2_top.xcor() - 30) and (player.xcor() - 10 < pipe2_top.xcor() + 30):
        if (player.ycor() + 10 > pipe2_top.ycor() - 180) or (player.ycor() - 30 < pipe2_bottom.ycor() + 180):
            pen.clear()
            pen.write("Game Over", move=False, align="left", font=("Arial", 16, "normal"))
            wn.update()
            time.sleep(3)
            # Reset score
            player.score = 0
            # Move Pipes Back
            pipe2_top.setx(300)
            pipe2_bottom.setx(300)
            pipe2_top.setx(600)
            pipe2_bottom.setx(600)
            # Move Player back
            player.goto(-200, 0)
            player.dy = 0
            # Clear the pen
            pen.clear()
            
    # Check for score        
    if pipe2_top.xcor() + 30 < player.xcor() - 10:
        player.score += pipe2_top.value
        pipe2_top.value = 0
        # Update highest score if needed
        if player.score > highest_score:
            highest_score = player.score
        # Update score display
        pen.clear()
        pen.write(f"Score: {player.score}  Highest: {highest_score}", move=False, align="center", font=("Arial", 32, "normal"))

wn.mainloop()

findall()