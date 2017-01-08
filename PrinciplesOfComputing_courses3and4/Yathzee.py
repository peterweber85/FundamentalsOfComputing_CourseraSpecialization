"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    print answer_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    sorted_hand = sorted(hand)
    #print sorted_hand
    
    diff_num = list()
    diff_score = list()
    for idx in sorted_hand:
        if idx not in diff_num:
            diff_num.append(idx)
    
    for idx_i in diff_num:
        count = 0
        for idx_j in hand:
            if idx_i == idx_j:
                count += 1
        diff_score.append(count*idx_i)    
    
    return max(diff_score)

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = set([])
    for idx in range(1,num_die_sides+1):
        outcomes.add(idx)
    
    remaining_possibilities = gen_all_sequences(outcomes,num_free_dice)
    
    all_possibilities = set([])
    for idx in remaining_possibilities:
        all_possibilities.add(held_dice+idx)
        
    scores = list()
    for idx in all_possibilities:
        #sorted_possibilities.add(tuple(sorted(idx)))        
        scores.append(score(tuple(idx)))	 
    
    return float(sum(scores))/len(scores)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    subsets = [()]
    for idx_i in hand:
        for idx_j in subsets:
            subsets = subsets +[tuple(idx_j)+(idx_i,)]    
    subsets = set(subsets)
    return subsets
   
def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    maximum = 0
    max_tuple = tuple()
    for hold in gen_all_holds(hand):
        num_free_dice = len(hand)-len(hold)
        expect = expected_value(hold, num_die_sides, num_free_dice)
        if expect > maximum:
            max_tuple = (expect,tuple(hold))
            maximum = expect        
    return max_tuple
           
def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (6, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

#run_example()
#hand = (6, 6, 6,1, 5)
#score(hand) 

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)

#held_dice = (5,5)
#length = 3
#num_free_dice = length-len(held_dice)
#num_die_sides = 6
#num_die_sides = 6
#hand = (1,3,3,3,4)
#strategy(hand, num_die_sides)

#print expected_value(held_dice, num_die_sides,num_free_dice)  




