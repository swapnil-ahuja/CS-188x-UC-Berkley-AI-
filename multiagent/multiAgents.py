# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        print "legalMoves",legalMoves[chosenIndex]

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        ghostPositions=successorGameState.getGhostPositions()






        "*** YOUR CODE HERE ***"
        print currentGameState.getPacmanPosition()
        print "current ghost",currentGameState.getGhostPositions()
        print "newPOs",newPos
        print "newFood",newFood.asList()
        #print "newGhostStates",newGhostStates
        
        print "ghost Position",ghostPositions
        print "newScaredTimes",newScaredTimes
        
        ghostdist=[]
        for gp in ghostPositions:
          ghostdist.append(abs(gp[0]-newPos[0])+abs(gp[1]-newPos[0]))

        if min(ghostdist)<3:
          wg=-10.0
        elif max(ghostdist)<3:
          wg=-20.0
        else:
          wg=10.0

        if newPos in ghostPositions:
          return -10000

        ghost=sum(ghostdist)
        if ghost!=0:
          ghost=1.0/ghost

        


        return (wg*ghost)


        #return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        final= self.value(gameState,0)
        print "-----------------------------final",final
        return final[0]
        
    def value(self,gs,depth):
      if depth==self.depth*gs.getNumAgents() or gs.isLose() or gs.isWin():
        print "Here Terminate"
        return ("NULL",self.evaluationFunction(gs))

      if depth % gs.getNumAgents()==0:
        print "Max enter---"
        return self.max(gs,depth)
      else:
        print "MIN enter"
        return self.min(gs,depth)





    def max(self,gs,depth):
      actions=gs.getLegalActions(self.index)

      print "MAX--"
      print actions
      if len(actions)==0:
        return ("NULL",self.evaluationFunction(gs))



      v=("NULL",-10000)
      
      for a in actions:
        print "Max a",a
        x=gs.generateSuccessor(self.index,a)
        
        z=self.value(x,depth+1)
        print "Max z1",a,z[1]
        if z[1]>v[1]:
          v=(a,z[1])
        #print gs.getNumAgents()
      print "MAX OUTPUT:-----",v
      return v
        




    def min(self,gs,depth):
      actions=gs.getLegalActions(depth%gs.getNumAgents())
      print "MIN"
      print actions
      if len(actions)==0:
        return ("NULL",self.evaluationFunction(gs))
      v=("NULL", 10000)
      for a in actions:
        print "Min a ",a
        x=gs.generateSuccessor(depth%gs.getNumAgents(),a)
        
        z=self.value(x,depth+1)
        #print "MIN z",z
        print "Min z1",a,z[1]
        if z[1]<v[1]:
          v=(a,z[1])
        #print gs.getNumAgents()
      print "MIN OUTPUT:",v
      return v




        

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        final= self.value(gameState,0,-10000,10000)
        print "-----------------------------final",final
        return final[0]
        
    def value(self,gs,depth,alpha,beta):
      if depth==self.depth*gs.getNumAgents() or gs.isLose() or gs.isWin():
        print "Here Terminate"
        return ("NULL",self.evaluationFunction(gs))

      if depth % gs.getNumAgents()==0:
        print "Max enter---"
        return self.max(gs,depth,alpha,beta)
      else:
        print "MIN enter"
        return self.min(gs,depth,alpha,beta)





    def max(self,gs,depth,alpha,beta):
      actions=gs.getLegalActions(self.index)

      print "MAX--"
      print alpha,beta
      print actions
      if len(actions)==0:
        return ("NULL",self.evaluationFunction(gs))



      v=("NULL",-10000)
      
      for a in actions:
        print "Max a",a
        x=gs.generateSuccessor(self.index,a)
        
        z=self.value(x,depth+1,alpha,beta)
        print "Max z1",a,z[1]
        if z[1]>v[1]:
          v=(a,z[1])
        if v[1]> beta:
          print "pruned==========="
          return v
        if v[1]>alpha:
          alpha=v[1]


        #print gs.getNumAgents()
      print "MAX OUTPUT:-----",v
      return v
        




    def min(self,gs,depth,alpha,beta):
      actions=gs.getLegalActions(depth%gs.getNumAgents())
      print "MIN"
      print alpha, beta
      print actions
      if len(actions)==0:
        return ("NULL",self.evaluationFunction(gs))
      v=("NULL", 10000)
      for a in actions:
        print "Min a ",a
        x=gs.generateSuccessor(depth%gs.getNumAgents(),a)
        
        z=self.value(x,depth+1,alpha,beta)
        #print "MIN z",z
        print "Min z1",a,z[1]
        if z[1]<v[1]:
          v=(a,z[1])
        if depth%gs.getNumAgents()!=0:
          if v[1]<alpha:
            print "pruned==========="
            return v 
          if beta>v[1]:
            beta=v[1]

        #print gs.getNumAgents()
      print "MIN OUTPUT:",v
      return v


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        final= self.value(gameState,0)
        print "-----------------------------final",final
        return final[0]
        
    def value(self,gs,depth):
      if depth==self.depth*gs.getNumAgents() or gs.isLose() or gs.isWin():
        print "Here Terminate"
        return ("NULL",self.evaluationFunction(gs))

      if depth % gs.getNumAgents()==0:
        print "Max enter---"
        return self.max(gs,depth)
      else:
        print "MIN enter"
        return self.min(gs,depth)





    def max(self,gs,depth):
      actions=gs.getLegalActions(self.index)

      print "MAX--"
      print actions
      if len(actions)==0:
        return ("NULL",self.evaluationFunction(gs))



      v=("NULL",-10000)
      
      for a in actions:
        print "Max a",a
        x=gs.generateSuccessor(self.index,a)
        
        z=self.value(x,depth+1)
        print "Max z1",a,z[1]
        if z[1]>v[1]:
          v=(a,z[1])
        #print gs.getNumAgents()
      print "MAX OUTPUT:-----",v
      return v
        




    def min(self,gs,depth):
      actions=gs.getLegalActions(depth%gs.getNumAgents())
      print "MIN"
      print actions
      if len(actions)==0:
        return ("NULL",self.evaluationFunction(gs))
      v=("NULL", 0)
      avg=0
      count=0
      for a in actions:
        print "Min a ",a
        x=gs.generateSuccessor(depth%gs.getNumAgents(),a)
        
        z=self.value(x,depth+1)
        #print "MIN z",z
        #print "Min z1",a,z[1]
        #if z[1]<v[1]:
          #v=(a,z[1])
        #print gs.getNumAgents()
        avg=avg + z[1]
        count=count+1

      
      x=(1.0*avg)/count
      v=("NULL",x)
      print "MIN OUTPUT:",v
      return v
       

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    score=currentGameState.getScore() #Positive
    
    pacmanPos=currentGameState.getPacmanPosition() 
    ghostPos=currentGameState.getGhostPositions() # Negative

    foodPos=currentGameState.getFood() #Positive
    foodNum=currentGameState.getNumFood() #Negative

    print "pacmanPos",pacmanPos
    print "ghostPos",ghostPos
    print "foodPos",foodPos.asList()
    print "foodNum",foodNum
    
    ghostdist=[]
    for gp in ghostPos:
      ghostdist.append(abs(gp[0]-pacmanPos[0])+abs(gp[1]-pacmanPos[0]))

    if min(ghostdist)<3:
      wg=-10.0
    elif max(ghostdist)<3:
      wg=-20.0
    else:
      wg=10.0

    ghost=sum(ghostdist)
    if ghost!=0:
      ghost=1.0/ghost

    food=0

    if pacmanPos in foodPos.asList():
      food=10.0

    if foodNum!=0:
      foodNum=1.0/foodNum
    elif foodNum==0:
      foodNum=100









    return score + (wg*ghost) + food +foodNum



























    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

