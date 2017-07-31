# Imports.
import numpy as np
import numpy.random as npr
from collections import Counter

from SwingyMonkey import SwingyMonkey

epsilon = 0.1
eta = 0.8
discount = 0.8

filename = 'SARSA' + '_greedy' + str(epsilon) + '_learn' + str(eta) + '_discount' + str(discount) + '.txt'

class Learner(object):


    def __init__(self):
        self.last_state  = None
        self.last_action = None
        self.last_reward = None

        self.q_values = Counter()
        # discount rate for next step-Qs
        self.discount = discount
        # eta the learning rate
        self.eta = eta
        # set epsilon-greedy parameter
        self.epsilon = {1: epsilon, 4: epsilon}
        self.gravity = 0
        self.new = True

        self.epoch = 0

    def reset(self):
        self.last_state  = None
        self.last_action = None
        self.last_reward = None
        self.new = True
        self.gravity = 0
        self.epoch +=1

    # screen width = 600 pixels
    # screen height = 400 pixels
    # total game screen = 400x600
    # velocity assumed to be mostly contained between -40 and 25
    # m_vel is velocity of the monkey discretized in 18 states
    # dist_to_tree is the distance of our monkey to the next tree 
    #                               (1 of 40 10-pixel buckets)
    # monkey_to_top is the distance from the tree top to the monkey top
    # monkey_to_bot is the distance from the monkey's bottom to the
    #                               tree's bottom 
    # We choose to discretize by vertical velocity of the monkey
    #   because this will help us theoretically learn to play better
    #   across games with different gravity settings
    def discretize_states(self, state, vel_size=10, pos_size=100):
        discrete_states = {}
        discrete_states['dist_to_next_tree'] = state['tree']['dist'] / pos_size
        discrete_states['monkey_to_top'] = (state['tree']['top'] - state['monkey']['top']) / pos_size
        discrete_states['monkey_to_bot'] = (state['monkey']['bot'] - state['tree']['bot']) / pos_size
        discrete_states['gravity'] = self.gravity
        return discrete_states

    # return Q value for given state and action
    def getQValue(self, state, action):
        return self.q_values[(tuple(state.values()), action)]

    # Q update
    # based on current state, update Q for last state and last action
    def update_Q(self, last_state, last_action, current_state, current_action, reward):
        last_q = self.getQValue(last_state, last_action)
        current_q = self.getQValue(current_state, current_action)
        gradient = last_q - (reward + self.discount * current_q)
        
        self.q_values[(tuple(last_state.values()), last_action)] = (last_q - 
            self.eta * gradient)

    # return policy under a given state
    def getMaxAction(self, state):
        return np.argmax([self.getQValue(state,i) for i in [0,1]])

    # gets the action to take given the current state
    # this is an epsilon-greedy implementation
    def getPolicy(self, state):
        # with probability 1-epsilon
        if npr.rand() < self.epsilon[self.gravity]:
            action = npr.choice([0, 1])
            self.epsilon[self.gravity] = self.epsilon[self.gravity] * 0.5
        else:
            # else choose optimal policy
            action = self.getMaxAction(state)

        return action


    def action_callback(self, state):
        '''
        Implement this function to learn things and take actions.
        Return 0 if you don't want to jump and 1 if you do.
        '''

        # You might do some learning here based on the current state and the last state.

        # You'll need to select and action and return it.
        # Return 0 to swing and 1 to jump.







        # get gravity
        if self.new and not (self.last_state is None ):
            self.gravity = self.last_state['monkey']['vel'] - state['monkey']['vel']
            self.new = False
        
        
        if self.last_state is None:
            # always let monkey swing at the first action of each epoch to get gravity
            current_action = 0
        else:
            last_state = self.discretize_states(self.last_state)
            current_state = self.discretize_states(state)
            # get current action according to policy
            current_action = self.getPolicy(current_state)

            self.update_Q(last_state, self.last_action, 
                current_state, current_action, self.last_reward)
            

        self.last_action = current_action
        self.last_state = state

        return self.last_action

    def reward_callback(self, reward):
        '''This gets called so you can see what reward you get.'''

        self.last_reward = reward


def run_games(learner, hist, iters = 100, t_len = 100):
    '''
    Driver function to simulate learning by having the agent play a sequence of games.
    '''
    f = open(filename, 'w')
    for ii in range(iters):
        # Make a new monkey object.
        swing = SwingyMonkey(sound=False,                  # Don't play sounds.
                             text="Epoch %d" % (ii),       # Display the epoch on screen.
                             tick_length = t_len,          # Make game ticks super fast.
                             action_callback=learner.action_callback,
                             reward_callback=learner.reward_callback)

        # Loop until you hit something.
        while swing.game_loop():
            pass

        # Save score history.
        line = 'epoch' + ':'+ str(ii) + ':' + str(swing.gravity) + ':' +str(swing.score)  + '\n' 
        print line
        f.write(line)

        hist.append(swing.score)

        # Reset the state of the learner.
        learner.reset()
    
    print 'best score:', np.max(hist)
    print 'average score:', np.mean(hist)
    print hist
    f.write('best score:' + str(np.max(hist)) + '\n')
    f.write('average score:' + str(np.mean(hist)) + '\n')
    return


if __name__ == '__main__':

	# Select agent.
	agent = Learner()

	# Empty list to save history.
	hist = []; 

	run_games(agent, hist, 500, 1)



