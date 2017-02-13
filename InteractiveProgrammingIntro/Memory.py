# implementation of card game - Memory

import simplegui
import random

pos_x = 50  
pos_y = 70
temp = []
card_pos0 = None
card_pos1 = None 
card_pos2 = None
mouseclick_pos = list()
numbers = range(0,8)
numbers.extend(numbers) 
exposed = list()
for l in range(0, len(numbers)):
        exposed.append(False)

# helper function to initialize globals
def new_game():
    global state, counter
    state = 0 
    counter = 0
    label.set_text("Turns = "+str(counter))
    random.shuffle(numbers)
    for l in range(0, len(numbers)):
        exposed[l]=False
    
     
# define event handlers
def mouseclick(pos):
    mouseclick_pos = pos
    card_pos = pos[0]/50 
    global state, card_pos0, card_pos1, exposed, counter                   
    
    if state == 0:
        state = 1
        print 'state ', state
        exposed[card_pos]=True
        card_pos0 = card_pos
        
    elif state == 1:
        if card_pos != card_pos0:
            state = 2
            print 'state ', state
            exposed[card_pos]=True
            card_pos1 = card_pos
    else:
        if card_pos != card_pos0 and card_pos != card_pos1:
            counter = counter + 1
            label.set_text("Turns = "+str(counter))
            state = 1
            print 'state ', state	
            exposed[card_pos]=True
            if numbers[card_pos0] != numbers[card_pos1]:
                exposed[card_pos0] = False
                exposed[card_pos1] = False
            card_pos0 = card_pos

           
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(numbers)):
        canvas.draw_polygon([[0+i*50, 0], [0+i*50, 100], [50+i*50, 100], [50+i*50, 0]], 5, 'White','Green')
        if exposed[i] == True:
            canvas.draw_text(str(numbers[i]), (pos_x*i + 10, pos_y), 50, 'White')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
