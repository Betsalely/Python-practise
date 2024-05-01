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
    else:
        print('aw man :(')
        
    

print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
mark = round(mark)
print('Marks obtained:',mark)
print('BYE!')
#ends the quiz












# import turtle as t
# playerAscore=0
# playerBscore=0
 
# #create a window and declare a variable called window and call the screen()
# window=t.Screen()
# window.title("The Pong Game")
# window.bgcolor("green")
# window.setup(width=800,height=600)
# window.tracer(0)
 
# #Creating the left paddle
# leftpaddle=t.Turtle()
# leftpaddle.speed(0)
# leftpaddle.shape("square")
# leftpaddle.color("white")
# leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
# leftpaddle.penup()
# leftpaddle.goto(-350,0)
 
# #Creating the right paddle
# rightpaddle=t.Turtle()
# rightpaddle.speed(0)
# rightpaddle.shape("square")
# rightpaddle.color("white")
# rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
# rightpaddle.penup()
# rightpaddle.goto(350,0)
 
# #Code for creating the ball
# ball=t.Turtle()
# ball.speed(10)
# ball.shape("circle")
# ball.color("red")
# ball.penup()
# ball.goto(5,5)
# ballxdirection=1
# ballydirection=1
 
# #Code for creating pen for scorecard update
# pen=t.Turtle()
# pen.speed(0)
# pen.color("Blue")
# pen.penup()
# pen.hideturtle()
# pen.goto(0,260)
# pen.write("score",align="center",font=('Arial',24,'normal'))
 
# #code for moving the leftpaddle
# def leftpaddleup():
#     y=leftpaddle.ycor()
#     y=y+90
#     leftpaddle.sety(y)
 
# def leftpaddledown():
#     y=leftpaddle.ycor()
#     y=y-90
#     leftpaddle.sety(y)
 
# #code for moving the rightpaddle
# def rightpaddleup():
#     y=rightpaddle.ycor()
#     y=y+90
#     rightpaddle.sety(y)
 
# def rightpaddledown():
#     y=rightpaddle.ycor()
#     y=y-90
#     rightpaddle.sety(y)
 
# #Assign keys to play
# window.listen()
# window.onkeypress(leftpaddleup,'w')
# window.onkeypress(leftpaddledown,'s')
# window.onkeypress(rightpaddleup,'Up')
# window.onkeypress(rightpaddledown,'Down')
 
# while True:
#     window.update()
 
#     #moving the ball
#     ball.setx(ball.xcor()+ballxdirection)
#     ball.sety(ball.ycor()+ballxdirection)
 
#     #border set up
#     if ball.ycor()>290:
#         ball.sety(290)
#         ballydirection=ballydirection*-1
#     if ball.ycor()<-290:
#         ball.sety(-290)
#         ballydirection=ballydirection*-1
         
#     if ball.xcor() > 390:
#         ball.goto(0,0)
#         ball_dx = ball_dx * -10
#         player_a_score = player_a_score + 1
#         pen.clear()
#         pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
#         os.system("afplay wallhit.wav&")
 
 
 
#     if(ball.xcor()) < -390: # Left width paddle Border
#         ball.goto(0,0)
#         ball_dx = ball_dx * -10
#         player_b_score = player_b_score + 1
#         pen.clear()
#         pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
#         os.system("afplay wallhit.wav&")
 
#      # Handling the collisions with paddles.
 
#     if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
#         ball.setx(340)
#         ball_dx = ball_dx * -1
#         os.system("afplay paddle.wav&")
 
#     if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
#         ball.setx(-340)
#         ball_dx = ball_dx * -1
#         os.system("afplay paddle.wav&")