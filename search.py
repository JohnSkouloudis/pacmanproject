# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    from util import Stack
    
    stack = Stack() #initialize stack

    visited = set() #visited states
    path = [] #the path of actions to reach from start to goal

    
    if problem.isGoalState(problem.getStartState()): #if start state is the same as goal state
        return []

    
    stack.push((problem.getStartState(), path))

    while(True):

        
        if stack.isEmpty():
            return []

        state, path = stack.pop() 
        visited.add(state) 

        
        if problem.isGoalState(state):
            return path

        #get the successors of the state
        succ = problem.getSuccessors(state)

        
        for item in succ:
            print(item[0],item[1],item[2])
            if item[0] not in visited: #if the state has not been visited
                newPath = path.copy()
                newPath.append(item[1]) #add the succ state to the path
                stack.push((item[0], newPath))#push the state and path to the stack
        print("end of for loop")
                

    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    from util import Queue
    queue=Queue()

    visited = set() # visited states 
    path = [] #the path of actions to reach from start to goal

    
    if problem.isGoalState(problem.getStartState()):#if start state is the same as goal state
        return []

    
    queue.push((problem.getStartState(), path))

    while(True):

        
        if queue.isEmpty():
            return []

        state, path = queue.pop() 
        visited.add(state) 

        
        if problem.isGoalState(state):
            return path

         #get the successors of the state
        succ = problem.getSuccessors(state)

        
        for item1 in succ:
            if item1[0] not in visited and item1[0] not in (item2[0] for item2 in queue.list):#if the state has not been visited and not in the queue
                newPath = path.copy()
                newPath.append(item1[1])#add the succ state to the path
                queue.push((item1[0], newPath))#push the state and path to the queue

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    from util import PriorityQueue

    pqueue = PriorityQueue() #initialize priority queue  

    visited = set() #visited states
    path = [] #the path of actions to reach from start to goal

    if problem.isGoalState(problem.getStartState()):#if start state is the same as goal state
        return []
    
    pqueue.push((problem.getStartState(), path), 0)

    while(True):
            
            
            if pqueue.isEmpty():
                return []
    
            state, path = pqueue.pop() 
            visited.add(state) 
    
            
            if problem.isGoalState(state):
                return path
    
            #get the successors of the state
            succ = problem.getSuccessors(state)
    
            
            for item1 in succ:
                print(item1[0],item1[1],item1[2])
                if item1[0] not in visited and item1[0] not in (item2[2][0] for item2 in pqueue.heap):
                    newPath = path.copy()
                    newPath.append(item1[1])
                    cost = problem.getCostOfActions(newPath)
                    pqueue.push((item1[0], newPath), cost)
                
                # If we find lower cost path for same state, update pqueue with lower cost path
                elif item1[0] in (item2[2][0] for item2 in pqueue.heap):
                    for item2 in pqueue.heap:
                        if item2[2][0] == item1[0]:
                            oldCost = problem.getCostOfActions(item2[2][1])

                    newCost = problem.getCostOfActions(path + [item1[1]])

                    if oldCost > newCost:
                        newPath = path + [item1[1]]
                        pqueue.update((item1[0], newPath), newCost)


    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    from util import PriorityQueue

    pqueue=PriorityQueue() #initialize priority queue

    visited=set() #visited states   
    path=[] #the path of actions to reach from start to goal

    if problem.isGoalState(problem.getStartState()):
        return []
    
    pqueue.push((problem.getStartState(), path), heuristic(problem.getStartState(), problem))

    while(True):

        
        if pqueue.isEmpty():
            return []

        state, path = pqueue.pop() 

        
        if state in visited:
            continue
        
        visited.add(state) 

        
        if problem.isGoalState(state):
            return path

        
        succ = problem.getSuccessors(state)

        
        for item in succ:
            if item[0] not in visited:

                newPath = path + [item[1]] # Fix new path
                g_cost = problem.getCostOfActions(newPath)
                h_cost = heuristic(item[0], problem)
                f_cost = g_cost + h_cost
                pqueue.push((item[0], newPath), f_cost)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
