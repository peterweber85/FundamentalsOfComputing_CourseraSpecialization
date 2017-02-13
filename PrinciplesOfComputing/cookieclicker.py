"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
#SIM_TIME = 10000000000.0
SIM_TIME = 1000000
BUILD_GROWTH = 1.1

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._cookies = 0.0
        self._time = 0.0
        self._cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return "Time: " + str(self._time) + " Current Cookies: " + str(self._cookies) + " CPS: " + str(self._cps) + " History: " + str(self._history)
        
            
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._cookies 
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies - self._cookies > 0:
            time_to_wait = math.ceil(float(cookies - self._cookies) / self._cps)
            return float(time_to_wait)
        else:
            return 0.0
            
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0:
            self._time += time
            self._cookies += time * self._cps
            self._total_cookies += time * self._cps
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        # update CPS
        if cost <= self._cookies: 
            self._cps += additional_cps
            self._cookies -= cost
            self._history = self._history + [(self._time, item_name, cost, self._total_cookies)]
        
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Replace with your code
    clicker = ClickerState()
    build_info_clone = build_info.clone()
    
    while duration - clicker.get_time() >= 0:
        item = strategy(clicker.get_cookies(), clicker.get_cps(), clicker.get_history(), duration - clicker.get_time(), build_info_clone)		
        if item is None:
            break 
        
        
        cost_in_cookies = build_info_clone.get_cost(item)
        time_to_wait = clicker.time_until(cost_in_cookies)
          
        if time_to_wait > duration - clicker.get_time():
            break
        else:
            clicker.wait(time_to_wait)
            clicker.buy_item(item, cost_in_cookies, build_info_clone.get_cps(item))
            build_info_clone.update_item(item)	
    
    clicker.wait(duration - clicker.get_time())	
    return clicker        
#Determine how much time must elapse until it is possible to purchase the item. If you would have to wait past the duration of the simulation
#to purchase the item, you should end the simulation.
    
    

def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return None

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    
    build_info_clone = build_info.clone()
    
    items = build_info_clone.build_items()
    
    costs = []
    for item in items:
        costs.append(build_info_clone.get_cost(item))
    
    cost_cheapest = min(costs)
    index_cheapest = costs.index(cost_cheapest)
    item_cheapest = items[index_cheapest]
    
    clicker = ClickerState()
    time_to_wait = clicker.time_until(cost_cheapest)
    
    if time_to_wait <= clicker.get_cookies() + time_left*clicker.get_cps():
        #print str(item_cheapest)
        return str(item_cheapest)
    else:
        #print None
        return None
        
    
def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    build_info_clone = build_info.clone()
    clicker = ClickerState()
        
    items = build_info_clone.build_items()
    
    costs = []
    for item in items:
        costs.append(build_info_clone.get_cost(item))
    
    tmp_costs = []
    tmp_items = []
    
    for idx in range(len(items)):
        if costs[idx] <= clicker.get_cookies() + time_left*clicker.get_cps():
            tmp_costs.append(costs[idx])
            tmp_items.append(items[idx])
    
    if tmp_items == []:
        return None
    else:
        cost = max(tmp_costs)
        index = tmp_costs.index(cost)
        item = tmp_items[index]
        return item  
            
            
        
def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
#run()
#cookies = 10000
#cps = 5
#history = (0.0, None, 0.0, 0.0)
#time_left = 100000
#build_info = provided.BuildInfo()
#build_clone = build_info.clone()

#strategy_expensive(cookies, cps, history, time_left, build_clone)
    
#class BuildInfo:
#    """
#    Class to track build information.
#    """
#    
#    def __init__(self, build_info = None, growth_factor = BUILD_GROWTH):
#        """
#        Initialize the BuildInfo object. Use default arguments for the game.
#        """
#            
#    def build_items(self):
#        """
#        Get a list of buildable items sorted by name.
#        """
#            
#    def get_cost(self, item):
#        """
#        Get the current cost of an item.
#        Will throw a KeyError exception if item is not in the build info.
#        """
#    
#    def get_cps(self, item):
#        """
#        Get the current CPS of an item
#        Will throw a KeyError exception if item is not in the build info.
#        """
#    
#    def update_item(self, item):
#        """
#        Update the cost of an item by the growth factor
#        Will throw a KeyError exception if item is not in the build info.
#        """
#        
#    def clone(self):
#        """
#        Return a clone of this BuildInfo
#        """	
