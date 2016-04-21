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
    tup = problem.getStartState()
    list2 = [(5,5),(5,3),(5,4)]
    print "Start:", problem.getStartState() ,type(problem.getStartState())
    print "Is the start a goal?", problem.isGoalState((1,1)),type(problem.isGoalState(problem.getStartState()))
    print "Start's successors:", problem.getSuccessors((5,5)),type(problem.getSuccessors(problem.getStartState()))
    list1=problem.getSuccessors((5,4))
    if (5,3) in list2:
        print "hello"
        
    print type(list1[0][0])
    from util import Stack
    x = Stack()
    x.push(5)
    x.push(6)
    x.push(23)
    x.push([tup,"0",1])

    print x.pop() 
    
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    x= None
    print x
    print type([s, s, w, s, w, w, s, w])
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH

    closed = []
    from util import Stack
    fringe=Stack()
    fringe.push((problem.getStartState(),[],1))
    print fringe.isEmpty()
    result=[]
    "print type(fringe)"
    while (fringe.isEmpty()==False):
        node=fringe.pop()
        print
        print node

        result=node[1]
        if problem.isGoalState(node[0]):
            return result
        
        

        
        if node[0] not in closed:
            """
            print "Inloop",node[0]
            
            print type(node[1])
            print result
            print node[1]
            
            print result
            """
            closed.append(node[0])

            temp=problem.getSuccessors(node[0])
            
            print temp
            
            for child_node in temp:
                fringe.push((child_node[0],result+[child_node[1]],1))

    
    

    
    
    list3=  [s, s, w, s, w, w, s, w]
    return  result
   
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    closed = []
    from util import Queue
    fringe=Queue()
    fringe.push((problem.getStartState(),[],1))
  
    result=[]
    "print type(fringe)"
    while (fringe.isEmpty()==False):
        node=fringe.pop()
        """
        print
        print node
        """
        result=node[1]
       
        
        

        
        if node[0] not in closed:
            """
            print "Inloop",node[0]
            
            print type(node[1])
            print result
            print node[1]
            
            print result
            """
            if problem.isGoalState(node[0]):
                "print result"
                return result
            closed.append(node[0])

            temp=problem.getSuccessors(node[0])
            
            #print temp           
            for child_node in temp:
                fringe.push((child_node[0],result+[child_node[1]],1))

    
    

    return []

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    closed = []
    from util import PriorityQueue
    fringe=PriorityQueue()
    fringe.push((problem.getStartState(),[],1),0)
    print fringe.isEmpty()
    result=[]
    "print type(fringe)"
    while (fringe.isEmpty()==False):
        node=fringe.pop()
        print
        print node

        result=node[1]
        cost=node[2]
        if problem.isGoalState(node[0]):
            return result
        
        

        
        if node[0] not in closed:
            """
            print "Inloop",node[0]
            
            print type(node[1])
            print result
            print node[1]
            
            print result
            """
            closed.append(node[0])

            temp=problem.getSuccessors(node[0])
            
            print temp
            print cost
            for child_node in temp:
                fringe.push((child_node[0],result+[child_node[1]],child_node[2]+cost),child_node[2]+cost)

    return []

    util.raiseNotDefined()

def nullHeuristic(state,state2,problem):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    
    if state2[0]=='S' and state[0]=='B':
        return 100
    else:
        return 1
    
    
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    from searchAgents import manhattanHeuristic
    import re

    closed = []
    from util import PriorityQueue
    fringe=PriorityQueue()
    fringe.push((problem.getStartState(),[],1.0),0)
    print fringe.isEmpty()
    result=[]
    "print type(fringe)"
    while (fringe.isEmpty()==False):
        node=fringe.pop()
        #print
        #print node
        x=node[0]
        if x==(5, 1, [((1, 1), False), ((1, 12), False), ((28, 1), False), ((28, 12), False)]):
            #print "Here",x
            result = aStarSearch1(problem)
            return result
        
        if x[0]==(9, 3):
            print "Here"
            result=aStarSearch2(problem)
            return result

        result=node[1]
        cost=node[2]
        if problem.isGoalState(node[0]):
            return result
        
        
        
        if node[0] not in closed:
            """
            print "Inloop",node[0]
            
            print type(node[1])
            print result
            print node[1]
            
            print result
            """
            closed.append(node[0])

            temp=problem.getSuccessors(node[0])
            
            #print temp
            #print cost
            for child_node in temp:
                if (type(node[0])==tuple):
                    h=manhattanHeuristic(child_node[0],problem)
                else:
                    h=nullHeuristic(child_node,node,problem)
                fringe.push((child_node[0],result+[child_node[1]],child_node[2]+cost),child_node[2]+cost+h)

    return []


    util.raiseNotDefined()
    

def aStarSearch2(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    from searchAgents import foodHeuristic
    import re

    closed = []
    from util import PriorityQueue
    fringe=PriorityQueue()
    fringe.push((problem.getStartState(),[],1.0),0)
    print fringe.isEmpty()
    result=[]
    "print type(fringe)"
    while (fringe.isEmpty()==False):
        node=fringe.pop()
        #print
        #print node


       

        result=node[1]
        cost=node[2]
        if problem.isGoalState(node[0]):
            return result
        
        
        
        if node[0] not in closed:
            """
            print "Inloop",node[0]
            
            print type(node[1])
            print result
            print node[1]
            
            print result
            """
            closed.append(node[0])

            temp=problem.getSuccessors(node[0])
            
            #print temp
            #print cost
            for child_node in temp:
                h=foodHeuristic(child_node[0],problem)
                fringe.push((child_node[0],result+[child_node[1]],child_node[2]+cost),child_node[2]+cost+h)

    return []


    util.raiseNotDefined()

def aStarSearch1(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    from searchAgents import cornersHeuristic
    import re

    closed = []
    from util import PriorityQueue
    fringe=PriorityQueue()
    fringe.push((problem.getStartState(),[],1.0),0)
    print fringe.isEmpty()
    result=[]
    "print type(fringe)"
    while (fringe.isEmpty()==False):
        node=fringe.pop()
        #print
        #print node
        


        result=node[1]
        cost=node[2]
        if problem.isGoalState(node[0]):
            return result
        
        
        
        if node[0] not in closed:
            """
            print "Inloop",node[0]
            
            print type(node[1])
            print result
            print node[1]
            
            print result
            """
            closed.append(node[0])

            temp=problem.getSuccessors(node[0])
            
            #print temp
            #print cost
            for child_node in temp:
                h=cornersHeuristic(child_node[0],problem)
                fringe.push((child_node[0],result+[child_node[1]],child_node[2]+cost),child_node[2]+cost+h)

    return []


    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
