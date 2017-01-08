"""
Student code for Word Wrangler game
"""

import math
import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    temp_list1 = []
    for item in list1:
        if item not in temp_list1:
            temp_list1.append(item)
    return temp_list1        
        
    

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    temp_list2 = []
    for item in list1:
        if item in list2:
            temp_list2.append(item)
            
    return temp_list2

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """ 
    temp_list1 = list1[:]
    temp_list2 = list2[:]
    list3 = []
    while len(temp_list1) > 0 and len(temp_list2) > 0:
        if temp_list1[0] <= temp_list2[0]:
            list3.append(temp_list1.pop(0))
        else:
            list3.append(temp_list2.pop(0))
    
    if len(temp_list1) == 0:
        list3 += temp_list2 
            
    if len(temp_list2) == 0:
        list3 += temp_list1       
    
    return list3        
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    half = len(list1)/2
    sub1 = list1[:half]
    sub2 = list1[half:]
    
    if len(list1) == 0 or len(list1) == 1:
        return list1
    
    return merge(merge_sort(sub1),merge_sort(sub2))
    
    

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return ['']
    
    rest = word[1:]
    first = word[0]
    rest_strings = gen_all_strings(rest)
          
    all_strings = []
       
    for rest_string in rest_strings:
        for idx_j in range(0,len(rest_string)+1):
            new_strings = rest_string[:idx_j] + first + rest_string[idx_j:]
            all_strings.append(new_strings)
        
    return gen_all_strings(word[1:]) + all_strings 

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

#word = 'ab'
#print gen_all_strings(word)
  
    
