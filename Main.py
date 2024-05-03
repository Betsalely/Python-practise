










def pong():
    import turtle as t
    import os
    player_a_score = 0
    player_b_score = 0
    
    # create a window and declare a variable called window and call the screen()
    window = t.Screen()
    window.title("The Pong Game")
    window.bgcolor("green")
    window.setup(width=800, height=600)
    window.tracer(0)
    
    # Creating the left paddle
    left_paddle = t.Turtle()
    left_paddle.speed(0)
    left_paddle.shape("square")
    left_paddle.color("white")
    left_paddle.shapesize(stretch_wid=5, stretch_len=1)
    left_paddle.penup()
    left_paddle.goto(-350, 0)
    
    # Creating the right paddle
    right_paddle = t.Turtle()
    right_paddle.speed(0)
    right_paddle.shape("square")
    right_paddle.color("white")
    right_paddle.shapesize(stretch_wid=5, stretch_len=1)
    right_paddle.penup()
    right_paddle.goto(350, 0)
    
    # Code for creating the ball
    ball = t.Turtle()
    ball.speed(10)
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.goto(5, 5)
    ballxdirection = 2
    ballydirection = 1.5
    
    # Code for creating pen for scorecard update
    pen = t.Turtle()
    pen.speed(0)
    pen.color("Blue")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("score", align="center", font=('Arial', 24, 'normal'))
    
    PADDLE_SPEED = 20
    
    def left_paddle_up():
        y = left_paddle.ycor()
        y += PADDLE_SPEED
        if y < 250:  # Adjust this value if needed to limit paddle movement
            left_paddle.sety(y)

    # Function to move the left paddle down smoothly
    def left_paddle_down():
        y = left_paddle.ycor()
        y -= PADDLE_SPEED
        if y > -240:  # Adjust this value if needed to limit paddle movement
            left_paddle.sety(y)

    # Function to move the right paddle up smoothly
    def right_paddle_up():
        y = right_paddle.ycor()
        y += PADDLE_SPEED
        if y < 250:  # Adjust this value if needed to limit paddle movement
            right_paddle.sety(y)

    # Function to move the right paddle down smoothly
    def right_paddle_down():
        y = right_paddle.ycor()
        y -= PADDLE_SPEED
        if y > -240:  # Adjust this value if needed to limit paddle movement
            right_paddle.sety(y)
    # Assign keys to play
    window.listen()
    window.onkeypress(left_paddle_up, 'w')
    window.onkeypress(left_paddle_down, 's')
    window.onkeypress(right_paddle_up, 'Up')
    window.onkeypress(right_paddle_down, 'Down')

    # Exit game on 'q' key press
    window.onkeypress(window.bye, 'q')
        
    while True:
        window.update()
    
        # moving the ball
        ball.setx(ball.xcor() + ballxdirection)
        ball.sety(ball.ycor() + ballydirection)
    
        # border set up
        if ball.ycor() > 290:
            ball.sety(290)
            ballydirection *=-1
        if ball.ycor() < -290:
            ball.sety(-290)
            ballydirection *= -1
            
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ballxdirection *= 0
            ballxdirection += 2
            player_a_score += 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score), align="center", font=('Monaco', 24, "normal"))
            os.system("afplay wallhit.wav&")
    
        if ball.xcor() < -390:  # Left width paddle Border
            ball.goto(0, 0)
            ballxdirection *= 0
            ballxdirection += 2
            player_b_score += 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score), align="center", font=('Monaco', 24, "normal"))
            os.system("afplay wallhit.wav&")
    
        # Handling the collisions with paddles.
        if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
            ball.setx(340)
            ballxdirection *= -1.2
            
            os.system("afplay paddle.wav&")
    
        if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
            ball.setx(-340)
            ballxdirection *= -1.2
        


            os.system("afplay paddle.wav&")



 
print('Welcome to Yair Python Quiz')
answer=input('Are you willing to play the Quiz ? (yes/no) :')
score=0
total_questions=3

if answer.lower()=='yes':
    #ask the user and saves it
    answer=input('Before we start what is your name?')
    name = answer.lower()

    #greets user and introduces quiz
    answer=input('Ok ' + name+ ':Are you ready to play the Quiz which asks about Python ? (yes/no) :')
    if answer.lower()=='yes':
        print('Ok sweet')
        #ask the user a question
        answer=input('Question 1: What is the name of the programming language this was coded in? ')
        if answer.lower()=='python':
            score += 1
            print('correct')
        else:
            #gives them the correct answer
            print('Wrong Answer :(, it was Python')
            
        print('Question 2:`how do you write hello in a terminal using python? `')
        print('A) print(hello)      B) Print(hello)')
        print('C) print(\'hello\')      D) Print(\"helo\")')
        answer=input('write one of the letters: ')
        if answer.lower()=='c':
            score += 1
            print('correct')
        else:
            
            print('Wrong Answer :(, it was C) print(\'hello\') s')

        answer = input('Last question before you leave, do you want to play pong yes/no: ')
        if answer.lower()=='yes':
            pong()
        else:
            print('ok :)')
    else:
        print('aw man :(')
        pong()
        
    

print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
mark = round(mark)
print('Marks obtained:',mark)
print('BYE!')
#ends the quiz
