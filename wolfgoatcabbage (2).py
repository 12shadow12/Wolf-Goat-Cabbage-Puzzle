from search import *
import random

class WolfGoatCabbage(Problem):

    #a constructor that sets the initial and goal states
    def __init__(self, initial=frozenset(['F','W','G','C']), goal=frozenset()):
        #gives us access to Problem's methods
        super().__init__(initial, goal)

    #a method goal_test(state) that returns True if the given state is a goal state
    def goal_test(self, state):
        # print(f'GOAL: {self.goal}')
        # print(f'{state==self.goal}')
        return state == self.goal

    #a method result(state, action) that returns the new state reached from the given state and the given action. Assume that the action is valid.
    def result(self, state, action):
        #you are given a state and the action that is going to be done to it
        #return us the new state

        new_state = set(state) 
        # print(f'New state from result: {new_state}')

        # print(f'Action to do: {action}')
        #assuming its valid, I think we can just do this

        if 'F' not in state:
            for value in action:
                new_state.add(value)
        else:
            for value in action:
                new_state.remove(value)

        # print(f'\nNew state after taking action: {frozenset(new_state)}')
        return frozenset(new_state)
        
    
    #a method actions(state) that returns a list of valid actions in the given state
    def actions(self, state):
        #you are given a state
        #your task is to figure out the possible actions from that state
        #actions would be of type list
        #the farmer always moves with us, so we can always include him
        actions = []

        if 'F' in state and 'W' in state and 'G' in state and 'C' in state:
            actions.append(frozenset(['F','G']))
        if 'W' in state and 'C' in state and 'F' not in state and 'G' not in state:
            actions.append(frozenset(['F']))
        if 'F' in state and 'W' in state and 'C' in state and 'G' not in state:
            actions.append(random.choice([frozenset(['C','F']), frozenset(['W','F'])]))
        if 'C' in state and 'F' not in state and 'G' not in state and 'W' not in state:
            actions.append(frozenset(['F','G']))
        if 'W' in state and 'F' not in state and 'G' not in state and 'C' not in state:
            actions.append(frozenset(['F','G']))
        if 'F' in state and 'W' in state and 'G' in state and 'C' not in state:
            actions.append(frozenset(['F','W']))
        if 'F' in state and 'G' in state and 'C' in state and 'W' not in state:
            actions.append(frozenset(['F','C']))
        if 'G' in state and 'F' not in state and 'C' not in state and 'W' not in state:
            actions.append(frozenset(['F']))
        if 'F' in state and 'G' in state and 'W' not in state and 'C' not in state:
            actions.append(frozenset(['F','G']))
        
        # print(f'All possible valid actions: {actions}')
        
        return actions

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
