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


    https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/
          let S be stack
      S.push( s )            //Inserting s in stack
      mark s as visited.
      while ( S is not empty):
          //Pop a vertex from stack to visit next
          v  =  S.top( )
         S.pop( )
         //Push all the neighbours of v in stack that are not visited
        for all neighbours w of v in Graph G:
            if w is not visited :
                     S.push( w )
                    mark w as visited

    """
    "*** YOUR CODE HERE ***"

    caminosPosibles = util.Stack()
    visitados = []
    caminosPosibles.push((problem.getStartState(), [])) #Estamos en la posicion inicial y hemos hecho [] movimientos en este camino
    visitados.append(problem.getStartState()[0]) #no es necesario realmente, pero lo añadimos a visitados por que si no volveriamos a el en cada uno de sus succesors para comprobar si es el final
                                              # luego mirariamos su succesors de nuevo, los cuales estarian ya visitados y bla bla bla... en resumen: perderiamos tiempo

    while not caminosPosibles.isEmpty():

        elementoActual,lista_movimientos = caminosPosibles.pop() #Cogemos el elemento y los movimientos hechos para llegar a el
        for successor in problem.getSuccessors(elementoActual):
            pos=successor[0]
            dir=successor[1]
            if pos not in visitados: #Si ya hemos visitado el elemento pasamos de el, por que ya estara en el camino que hemos recorrido
                if(problem.isGoalState(pos)):
                    actualizada = lista_movimientos + [dir] #podemos ahorrarnos estas dos lineas y returnear directamene el append
                    #print(actualizada)
                    return(actualizada)
                else:
                    actualizada = lista_movimientos + [dir] #podemos ahorrarnos estas dos lineas y returnear directamene el append
                    #print(actualizada)
                    caminosPosibles.push((pos, actualizada)) #lo haria con arrays de numpy pero el coste de hacer un append en python es O(1) asi que solo haria el programa mas lento
                    #Dejo el codigo de todas formas por si en el futuro necesitamos usar arrays de numpy para optimizar otros ejercicios
                    ##caminosPosibles.push((pos, np.append(np.array(lista_movimientos),np.array(dir).tolist())))
                    visitados.append(pos)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
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
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
