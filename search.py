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
import heapq

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


    """
    Pseudocode from http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/dfs.html
       Set all nodes to "not visited";

   s = new Stack();    ******* Change to use a stack

   s.push(initial node);    ***** Push() stores a value in a stack

   while ( s ≠ empty ) do
   {
      x = s.pop();         ****** Pop() remove a value from the stack

      if ( x has not been visited )
      {
         visited[x] = true;         // Visit node x !

         for ( every edge (x, y)  /* we are using all edges ! */ )    
            if ( y has not been visited )   
	       s.push(y);       ***** Use push() !
      }
   }
    """
    caminos_posibles, caminoFinal = (util.Stack() for i in range(2)) #Asi es mas facil cambiar la estructura de todos a la vez
    caminos_posibles.push(problem.getStartState())
    visitados, camino = ([] for i in range(2)) #Esto es como antes pero con un array vacio
    actual = caminos_posibles.pop()
    while not problem.isGoalState(actual): #si no hemos terminado
        if actual not in visitados:
            visitados.append(actual)
            successors = problem.getSuccessors(actual)
            #print(successors)
            for siguiente,direccion,coste in successors: #son tres valores, las coordenadas, la direccion y el coste (creo?). si no pongo la ultima variable sale too many values to unpack (expected 2)
                if siguiente not in visitados:
                    caminos_posibles.push(siguiente) # meto sus coordenadas y el camino en los Stacks correspondientes
                    foo = camino + [direccion]
                    caminoFinal.push(foo) #lo mismo que antes (es importante que ambas pilas vayan sincronizadas, si hago push en una, hago push en la otra tambien
        actual = caminos_posibles.pop() #paso al siguiente nodo (coordenadas) posible
        camino = caminoFinal.pop() #y recupero su camino tambien
    return camino
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    caminos_posibles, caminoFinal = (util.Queue() for i in range(2)) #Asi es mas facil cambiar la estructura de todos a la vez
    caminos_posibles.push(problem.getStartState())
    visitados, camino = ([] for i in range(2))
    actual = caminos_posibles.pop()
    while not problem.isGoalState(actual): #si no hemos terminado
        if actual not in visitados:
            visitados.append(actual)
            successors = problem.getSuccessors(actual)
            #print(successors)
            for siguiente,direccion,coste in successors: #son tres valores, las coordenadas, la direccion y el coste (creo?). si no pongo la ultima variable sale too many values to unpack (expected 2)
                if siguiente not in visitados:
                    caminos_posibles.push(siguiente) # meto sus coordenadas y el camino en los Stacks correspondientes
                    foo = camino + [direccion]
                    caminoFinal.push(foo) #lo mismo que antes (es importante que ambas pilas vayan sincronizadas, si hago push en una, hago push en la otra tambien
        actual = caminos_posibles.pop() #paso al siguiente nodo (coordenadas) posible
        camino = caminoFinal.pop() #y recupero su camino tambien
    return camino
def uniformCostSearch(problem):
    # Se hace uso del módulo HeapQ (https://docs.python.org/2/library/heapq.html) para implementar una cola con prioridad

    estadosDirecciones = util.PriorityQueue()
    estadosDirecciones.push((problem.getStartState(), []), 0)

    visitados = []
    visitados.append(problem.getStartState())

    while not estadosDirecciones.isEmpty():
        estado, direcciones = estadosDirecciones.pop()

        if problem.isGoalState(estado):
            return direcciones

        if estado not in visitados:
            visitados.append(estado)

        for prox in problem.getSuccessors(estado):

            proxEstado = prox[0]
            proxDireccion = prox[1]

            if proxEstado not in visitados:
                direccionesNuevas = direcciones + [proxDireccion]
                prioridad = problem.getCostOfActions(direccionesNuevas)

                for index, (p, c, i) in enumerate(estadosDirecciones.heap):

                    if i[0] == proxEstado:

                        if p <= prioridad:
                            break

                        del estadosDirecciones.heap[index]
                        estadosDirecciones.heap.append((prioridad, c, (proxEstado, direccionesNuevas)))
                        # Heapify transforma la lista en una cola con prioridad
                        heapq.heapify(estadosDirecciones.heap)
                        break
                else:
                    estadosDirecciones.push((proxEstado, direccionesNuevas), prioridad)


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
