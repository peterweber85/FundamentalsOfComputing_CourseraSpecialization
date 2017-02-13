# template for "Stopwatch: The Game"
import simplegui
# define global variables
t = 0
output = str()

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global output
    D = t%10
    BC = t%600/10
    A = t%3600/600
    if BC < 10:
        BC = str(0)+str(BC)
        output = str(A)+":"+BC+":"+str(D)
    else:
        output = str(A)+":"+str(BC)+":"+str(D)
    

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    
def stop_handler():    
    timer.stop()
    
def reset_handler():
    global t
    t = 0
    draw_handler(canvas)
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t = t + 1
    format(t)

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(output,(100,100),30,'Blue')
    
# create frame
frame = simplegui.create_frame('Testing', 300, 200, 200)

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)
frame.add_button('Start', start_handler)
frame.add_button('Stop', stop_handler)
frame.add_button('Reset', reset_handler)

# start frame
frame.start()
# Please remember to review the grading rubric
