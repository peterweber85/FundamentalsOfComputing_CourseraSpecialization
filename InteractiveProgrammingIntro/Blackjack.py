# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
score_initial = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    def cover(self, canvas, pos):
        card_loc = (CARD_CENTER[0], 
                    CARD_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
      
    
# define hand class
class Hand:
    def __init__(self):
        self.cards_in_hand = []
        
    def __str__(self):
        hand_str = ""
        for i in range(len(self.cards_in_hand)):
            hand_str += str(self.cards_in_hand[i]) + " "
        return "Hand contains " + hand_str
        
    def add_card(self, card):
        self.cards_in_hand.append(card)
        
    def get_value(self):
        hand_value = []
        A_in_hand = False
        for i in range(len(self.cards_in_hand)):
            hand_value.append(VALUES[Card.get_rank(self.cards_in_hand[i])])
            if 'A' in Card.get_rank(self.cards_in_hand[i]):
                A_in_hand = True
        
        if not A_in_hand:
            return sum(hand_value)
        else:
            if sum(hand_value)<= 11:
                return sum(hand_value)+10
            else:
                return sum(hand_value)
        
        
    def draw(self, canvas, pos):
        for i in range(len(self.cards_in_hand)):
            pos[0] += 100
            Card.draw(self.cards_in_hand[i], canvas,pos)
    
    def cover(self, canvas, pos):
        Card.cover(self.cards_in_hand[0], canvas, pos)        
        
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.deck.append(Card(SUITS[i], RANKS[j]))

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        deck_str = ""
        for i in range(len(self.deck)):
            deck_str += str(self.deck[i]) + " "
        return "Deck contains " + deck_str       

#define event handlers for buttons
def deal():
    global d, dealer_hand, player_hand, outcome, in_play, score, score_initial
    d = Deck()
    d.shuffle()
    dealer_hand = Hand()
    player_hand = Hand()
    
        
    for i in range(2):
        dealer_hand.add_card(d.deal_card())
        player_hand.add_card(d.deal_card())

    print 'Dealer ', dealer_hand
    print 'Player ', player_hand
    in_play = True
    
    if score_initial:
        if outcome == False:
            score -= 1
        else:
            score += 1
    score_initial = True
    
    
def hit():
    global in_play, outcome
    if player_hand.get_value() <= 21:
        player_hand.add_card(d.deal_card())
        if dealer_hand.get_value() < player_hand.get_value():
            outcome = True
        elif dealer_hand.get_value() > player_hand.get_value():
            outcome = False
        
        if player_hand.get_value() > 21:
            print "You have busted"
            in_play = False
            outcome = False
    else:
        in_play = False
        outcome = False
    
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play
    in_play = False	# replace with your code below
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    pos_player = [0, 200]
    pos_dealer = [0, 400]
    card = Card("S", "A")
    dealer_hand.draw(canvas, pos_player)
    player_hand.draw(canvas, pos_dealer)
    canvas.draw_text('Dealer', [100, 180], 40, 'Black')
    canvas.draw_text('Player', [100, 380], 40, 'Black')
    canvas.draw_text('Blackjack',[200, 50], 40, 'Black')
    canvas.draw_text('score '+str(score),[350, 180], 30, 'Black')
    if in_play == True:
        dealer_hand.cover(canvas, pos_player)
        canvas.draw_text('Hit or Stand?', [250, 380], 40, 'Black')
    else:
        canvas.draw_text('New Deal?', [200, 100], 40, 'Black')
        if outcome == True:
            canvas.draw_text('You won', [250, 380], 40, 'Black')
        else:
            canvas.draw_text('You lost', [250, 380], 40, 'Black')

            
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()


