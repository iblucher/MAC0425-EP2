import util
from state import State

def successor(state, action):
    ''' Return the sucessor state generated by executing `action` in `state`. '''
    successor_state = state.union(action.pos_effect).difference(action.neg_effect)
    return successor_state

def validate(problem, solution):
    '''
    Return true if `solution` is a valid plan for `problem`.
    Otherwise, return false.

    OBSERVATION: you should check action applicability,
    next-state generation and if final state is indeed a goal state.
    It should give you some indication of the correctness of your planner,
    mainly for debugging purposes.
    '''
    state = problem.init
    for action in solution:
        successor_state = successor(state, action)
        state = successor_state
    if problem.goal.issubset(state):
        return True
    return False
