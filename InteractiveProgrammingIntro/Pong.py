# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
#ball_vel = []
#print type(ball_pos)
paddle1_pos = 100
paddle2_pos = 100 
paddle_vel = 0    
paddle1_vel = 0
paddle2_vel = 0
timestep = 0    
    
direction = int()
time = float()
hor_vel = int()
ver_vel = int()
score1 = 0
score2 = 0

def button_handler():
    global score1, score2
    score1 = 0
    score2 = 0
    new_game()

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    hor_vel = random.randrange(2, 4)
    ver_vel = random.randrange(1, 3)
    
    if direction == 0:
        ball_vel = [hor_vel, -ver_vel]
    else:
        ball_vel = [-hor_vel,-ver_vel]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    direction = random.randint(0,1)
    spawn_ball(direction)
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, time
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    #update ball
    ball_pos[0] += ball_vel[0]*(time+1)
    ball_pos[1] += ball_vel[1]*(time+1)        
    
    if ball_pos[0]+BALL_RADIUS>=WIDTH-PAD_WIDTH: 
        ball_vel[0]= -ball_vel[0]
        
        if ball_pos[1]>paddle2_pos+PAD_HEIGHT/2 or ball_pos[1]<paddle2_pos-PAD_HEIGHT/2:
            direction = random.randint(0,1)
            time = 0
            spawn_ball(direction)		
            score1 += 1
            
    if ball_pos[0]-BALL_RADIUS<=PAD_WIDTH:
        ball_vel[0]= -1.1*ball_vel[0]    
        
        if ball_pos[1]>paddle1_pos+PAD_HEIGHT/2 or ball_pos[1]<paddle1_pos-PAD_HEIGHT/2:
            direction = random.randint(0,1)
            time = 0
            spawn_ball(direction)
            score2 += 1
            
    if ball_pos[1]+BALL_RADIUS>=HEIGHT or ball_pos[1]-BALL_RADIUS<=0:
        ball_vel[1]= -1.1*ball_vel[1]
    
    # draw ball
    canvas.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 4, 'Green')
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + PAD_HEIGHT/2 > HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT/2
    elif paddle1_pos - PAD_HEIGHT/2 < 0:    
        paddle1_pos = PAD_HEIGHT/2
    else:    
        paddle1_pos += paddle1_vel
    
    if paddle2_pos + PAD_HEIGHT/2 > HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT/2
    elif paddle2_pos - PAD_HEIGHT/2 < 0:    
        paddle2_pos = PAD_HEIGHT/2
    else:    
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos-PAD_HEIGHT/2],
     [0, paddle1_pos+PAD_HEIGHT/2], [PAD_WIDTH, paddle1_pos+PAD_HEIGHT/2],
      [PAD_WIDTH, paddle1_pos-PAD_HEIGHT/2]], 3, 'Blue')
    canvas.draw_polygon([[WIDTH, paddle2_pos-PAD_HEIGHT/2],
     [WIDTH, paddle2_pos+PAD_HEIGHT/2], [WIDTH-PAD_WIDTH, paddle2_pos+PAD_HEIGHT/2],
      [WIDTH-PAD_WIDTH, paddle2_pos-PAD_HEIGHT/2]], 3, 'Blue')
    
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), [150, 50], 50, 'White')
    canvas.draw_text(str(score2), [450, 50], 50, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    paddle_vel = 5
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_vel
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel 
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_vel    
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    paddle_vel = 0
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_vel
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel 
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_vel   
     
        
def timer_handler():
    global time
    time = time + timestep
    #print time
    
timer = simplegui.create_timer(1000, timer_handler)
timer.start()
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', button_handler)

# start frame
new_game()
frame.start()
timer.start()
