import sys
import util


def h_naive(state, planning):
    return 0


def h_add(state, planning):
    '''
    Return heuristic h_add value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    '''
    Obter p inicial: zerar os átomos p que fazem parte do (state e da meta) e
    todos os outros átomos que fazem parte do estado também são zerados. Todos os
    outros átomos da meta recebem infinito.
    '''
    h = {}
    for p in state:
        h[p] = 0
    for p in planning.problem.goal:
        if p not in state:
            h[p] = sys.maxsize
    X = state
    while condition:
        for action in planning.applicable(X):
            pos = action.pos_effect
            X = X.union(pos)
            # soma dos custos das pré-condições da ação
            for precond in action.precond:
                # caso o átomo não tenha valor atribuído, atribua "infinito"
                if h[precond] != 0 and h[precond] != sys.maxsize:
                    h[precond] = sys.maxsize
                s = s + h[precond]
            for q in pos:
                if(h[q] > s + 1):
                    h[q] = s + 1
                    condition = True
                else:
                    condition = False
    for p in planning.problem.goal:
        res = res + h[p]
    return res






def h_max(state, planning):
    '''
    Return heuristic h_max value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    h = {}
    for p in state:
        h[p] = 0
    for p in planning.problem.goal:
        if p not in state:
            h[p] = sys.maxsize
    X = state
    while condition:
        for action in planning.applicable(X):
            pos = action.pos_effect
            X = X.union(pos)
            # soma dos custos das pré-condições da ação
            for precond in action.precond:
                # caso o átomo não tenha valor atribuído, atribua "infinito"
                if h[precond] != 0 and h[precond] != sys.maxsize:
                    h[precond] = sys.maxsize
                s = s + h[precond]
            for q in pos:
                if(h[q] > s + 1):
                    h[q] = s + 1
                    condition = True
                else:
                    condition = False
    for p in planning.problem.goal:
        res = res + h[p]
    return res 


def h_ff(state, planning):
    '''
    Return heuristic h_ff value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    util.raiseNotDefined()
    ' YOUR CODE HERE '
