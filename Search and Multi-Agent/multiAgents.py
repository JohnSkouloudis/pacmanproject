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

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # Find best action of agent 0 (Pacman) depending on the min value of ghost 1 etc
        bestValue = float('-inf')
        legalActions = gameState.getLegalActions(0)
        for action in legalActions:
            value = self.minValue(gameState.generateSuccessor(0, action), 0, 1)
            if value > bestValue:
                bestValue = value
                bestAction = action

        
        return bestAction

        util.raiseNotDefined()
    
    def maxValue(self, gameState, depth):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)

        # Get successors
        legalActions = gameState.getLegalActions(0)
        successorStates = [gameState.generateSuccessor(0, a) for a in legalActions]

        # Get max of minValue of the first ghost 
        return max(self.minValue(state, depth, 1) for state in successorStates)


    
    def minValue(self, gameState, depth, index):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)

        # Get successors
        legalActions = gameState.getLegalActions(index)
        successorStates = [gameState.generateSuccessor(index, a) for a in legalActions]

        ghostsNum = gameState.getNumAgents() - 1

        # If it's the last ghost go to the next depth else go to index + 1
        if index == ghostsNum:
            return min(self.maxValue(state, depth + 1) for state in successorStates)
        else:
            return min(self.minValue(state, depth, index + 1) for state in successorStates)

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        # Find best action of agent 0 (Pacman) depending on the min value of ghost 1 etc
        a = float('-inf')
        b = float('inf')
        bestValue = float('-inf')
        legalActions = gameState.getLegalActions(0)
        for action in legalActions:
            value = self.minValue(gameState.generateSuccessor(0, action), 0, 1, a, b)
            if value > bestValue:
                bestValue = value
                bestAction = action
                a = max(a, value)
        return bestAction

        util.raiseNotDefined()
    
    def maxValue(self, gameState, depth, a, b):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)

        # Get legal actions
        legalActions = gameState.getLegalActions(0)

        

        maxValue = float('-inf')
        for action in legalActions:
            successor = gameState.generateSuccessor(0, action)
            # Get max of minValue of the first ghost 
            maxValue = max(maxValue, self.minValue(successor, depth, 1, a, b))
            # alpha-beta pruning
            # if '>=' used unnecessary nodes expanded
            if maxValue > b:
                return maxValue
            a = max(a, maxValue) 
        return maxValue

    def minValue(self, gameState, depth, index, a, b):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)

        # Get legal actions
        legalActions = gameState.getLegalActions(index)

        ghostsNum = gameState.getNumAgents() - 1
        
        minValue = float('inf')
        for action in legalActions:
            successor = gameState.generateSuccessor(index, action)
            # If it's the last ghost go to the next depth else go to index + 1
            if index == ghostsNum:
                minValue = min(minValue, self.maxValue(successor, depth + 1, a, b))
            else:
                minValue = min(minValue, self.minValue(successor, depth, index + 1, a, b))
            # alpha-beta pruning
            # if '<=' used unnecessary nodes expanded
            if minValue < a:
                return minValue
            b = min(b, minValue)
        return minValue

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
         # Find best action of agent 0 (Pacman) depending on the min value of ghost 1 etc
        bestValue = float('-inf')
        legalActions = gameState.getLegalActions(0)
        for action in legalActions:
            value = self.expValue(gameState.generateSuccessor(0, action), 0, 1)
            if value > bestValue:
                bestValue = value
                bestAction = action
        return bestAction

        util.raiseNotDefined()

    def maxValue(self, gameState, depth):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)

        # Get successors
        legalActions = gameState.getLegalActions(0)
        successorStates = [gameState.generateSuccessor(0, a) for a in legalActions]

        return max(self.expValue(state, depth, 1) for state in successorStates)

    def expValue(self, gameState, depth, index):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)

        # Get successors
        legalActions = gameState.getLegalActions(index)
        successorStates = [gameState.generateSuccessor(index, a) for a in legalActions]

        ghostsNum = gameState.getNumAgents() - 1

        # If it's the last ghost go to the next depth else go to index + 1
        if index == ghostsNum:
            # Calculate the average value for chance node (expectimax) (sum of values / number of successors)
            return sum(self.maxValue(state, depth + 1) for state in successorStates) / len(successorStates)
        else:
            return sum(self.expValue(state, depth, index + 1) for state in successorStates) / len(successorStates)

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    from util import manhattanDistance

    evalScore = 0
    winScore = 99999999
    loseScore = -99999999
    foodDistScore = -1
    capsuleDistScore = -5
    scaredGhostDistScore = -10
    ghostDistScore = 5

    # win/loss
    if currentGameState.isWin():
        evalScore += winScore
    elif currentGameState.isLose():
        evalScore += loseScore
    
    pacmanPosition = currentGameState.getPacmanPosition()
    ghostStates = currentGameState.getGhostStates()
    ghostPositions = currentGameState.getGhostPositions()
    ghostScaredTime = [ghostState.scaredTimer for ghostState in ghostStates]
    food = currentGameState.getFood().asList()
    capsules = currentGameState.getCapsules()

    # food existing and food distance
    for pos in food:
        evalScore -= 15
        evalScore += manhattanDistance(pos, pacmanPosition) * foodDistScore

    # capsules existing and capsules distance
    for pos in capsules:
        evalScore -= 5
        evalScore += manhattanDistance(pos, pacmanPosition) * capsuleDistScore * len(capsules)

    # scared and normal ghost distances
    for pos, time in zip(ghostPositions, ghostScaredTime):
        if time > 0:
            evalScore += manhattanDistance(pos, pacmanPosition) * scaredGhostDistScore
        else:
            evalScore += manhattanDistance(pos, pacmanPosition) * ghostDistScore

    return evalScore

    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
