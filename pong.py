# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 800
HEIGHT = 450       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 100
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2, HEIGHT/2]
LEFT = False
RIGHT = True
game_ends = False
game_start = False
speed_select = False

# initialize paddle position
paddle1_pos1 = [HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]
paddle1_pos2 = [HALF_PAD_WIDTH, HEIGHT/2 + HALF_PAD_HEIGHT]
paddle2_pos1 = [(WIDTH - HALF_PAD_WIDTH), HEIGHT/2 - HALF_PAD_HEIGHT]
paddle2_pos2 = [(WIDTH - HALF_PAD_WIDTH), HEIGHT/2 + HALF_PAD_HEIGHT]

paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
ball_vel = [0, 0]
ball_accln = 1.1
var_vel = [0, 0]
lower = 0
upper = 0

# variable to keep track of the score
Player1_sc = 0
Player2_sc = 0

score_limit = 5
message = ""

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, var_vel, lower, upper
    global game_start, message, game_ends
    
    message = ""
    ball_pos = [WIDTH/2, HEIGHT/2]
   
    if direction == "RIGHT":
        ball_vel[0] = random.randrange(lower, upper)
        ball_vel[1] = -random.randrange(lower, upper)
    else:
        ball_vel[0] = -random.randrange(lower, upper)
        ball_vel[1] = -random.randrange(lower, upper)
        

    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global Player1_sc, Player2_sc
    global score_limit, message, game_ends, game_start, ball_vel

    Player1_sc = 0
    Player2_sc = 0
    
    direction = ["RIGHT", "LEFT", "RIGHT", "LEFT" ]
    
    if (game_start):
        spawn_ball(direction[random.randrange(0,4)])
    
        

def draw(canvas):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel,ball_accln, Player1_sc, Player2_sc
    global score_limit, message, game_ends, game_start
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos1[1] += paddle1_vel
    paddle1_pos2[1] += paddle1_vel
    
    paddle2_pos1[1] += paddle2_vel
    paddle2_pos2[1] += paddle2_vel
    
    if (paddle1_pos1[1] <= 0 or paddle1_pos2[1] >= HEIGHT):
        paddle1_vel = 0

    if (paddle2_pos1[1] <= 0 or paddle2_pos2[1] >= HEIGHT):
        paddle2_vel = 0
    
    # Update ball position upon hitting the floor and ceiling 
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
            
    # determine whether ball hit the gutters and spawn the ball
    # determine whether paddle and ball collide 
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] in range(paddle1_pos1[1], paddle1_pos2[1] + 1):
            ball_vel[0] = - (ball_vel[0] * ball_accln)
        else:
            Player2_sc += 1
            spawn_ball("RIGHT")
                
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] in range(paddle2_pos1[1], paddle2_pos2[1] + 1):
            ball_vel[0] = - (ball_vel[0] * ball_accln)
        else:
            Player1_sc += 1
            spawn_ball("LEFT")
     

    
    # draw paddles
    canvas.draw_line(paddle1_pos1, paddle1_pos2, PAD_WIDTH, "deepskyblue")    
    canvas.draw_line(paddle2_pos1, paddle2_pos2, PAD_WIDTH, "Red")
    
       
    
    # draw scores
    canvas.draw_text('Player 1', (150, 30), 24, 'Red', "sans-serif")
    canvas.draw_text('Player 2', (550, 30), 24, 'deepskyblue', "sans-serif")
    canvas.draw_text(str(Player1_sc), (180, 60), 24, 'Red')
    canvas.draw_text(str(Player2_sc), (580, 60), 24, 'deepskyblue')
    
    #check who is the winner and set the message
    if (Player1_sc == score_limit) or (Player2_sc == score_limit):
        if (Player1_sc > Player2_sc):
            message = "Game Over. Player 1 Wins!"
        else:
            message = "Game Over. Player 2 Wins!"
        game_ends = True
        game_start = False
        stop()
        reset()
        
    canvas.draw_text(message, (212, 235), 36, 'green')
    if (game_start == False):
        canvas.draw_text("Hit Space to start the game", (212, 140), 36, 'green')
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    global paddle1_pos1, paddle1_pos2
    global paddle2_pos1, paddle2_pos2, game_start
    shift = 5
    
    #Left paddle control
    if key == simplegui.KEY_MAP["W"] and paddle1_pos1[1] > 0:
        paddle1_vel -= shift              
    elif key == simplegui.KEY_MAP["S"] and paddle1_pos2[1] < HEIGHT:
        paddle1_vel += shift
            
    #Right paddle control
    if key == simplegui.KEY_MAP["up"] and paddle2_pos1[1] > 0:
        paddle2_vel -= shift
    elif key == simplegui.KEY_MAP["down"] and paddle2_pos2[1] < HEIGHT:
        paddle2_vel += shift
        
    if key == simplegui.KEY_MAP['space'] and (game_start == False):
        if (speed_select):
            game_start = True
            new_game()
            
        
def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["W"]:
        paddle1_vel = 0        
    elif key == simplegui.KEY_MAP["S"]:
        paddle1_vel = 0

    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
        
def reset():
    global game_start, game_ends, ball_pos
    global Player1_sc, Player2_sc
    game_start = False
    game_ends = False
    stop()
    
def stop():
    global ball_pos, ball_vel, message
    global Player1_sc, Player2_sc
    ball_vel = [0, 0]
    ball_pos = [WIDTH/2, HEIGHT/2]
    Player1_sc = 0
    Player2_sc = 0
    

def Novice():
    global lower, upper, speed_select
    lower = random.randrange(60, 90)/20
    upper = random.randrange(90, 120)/20
    speed_select = True
    new_game()

def Proficient():
    global lower, upper, speed_select
    lower = random.randrange(120, 150)/20
    upper = random.randrange(150, 180)/20
    speed_select = True
    new_game()
    
def Legend():
    global lower, upper, speed_select
    lower = random.randrange(180, 210)/20
    upper = random.randrange(210, 240)/20
    speed_select = True
    new_game()
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
label1 = frame.add_label(' ')
label1 = frame.add_label('First select the Speed level of the Ball', 150)
label1 = frame.add_label(' ')
button1 = frame.add_button("Novice", Novice, 70)
button1 = frame.add_button("Proficient", Proficient, 70)
button1 = frame.add_button("Legend", Legend, 70)
label1 = frame.add_label(' ')
label1 = frame.add_label(' ')
label1 = frame.add_label('Click Restart to reset the scores', 110)
label1 = frame.add_label(' ')
button1 = frame.add_button("Restart", reset)


# start frame
frame.start()