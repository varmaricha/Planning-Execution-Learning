# -*- coding: utf-8 -*-
"""
Created on Sun Oct 09 03:22:52 2016

@author: richa_000
"""

import numpy as np
import copy

class State(object):
    position = []
    def __init__(self, position):
        self.position = position

class LunarLockout:
    def __init__(self, init_state):
        self.init_state = init_state        
        self.labels = ['r','g','o','p','y','b']
        self.direction = ['up', 'down', 'left', 'right']
        self.num_objs = self.init_state.position.__len__()

    def getNodeID(self, state):
        state_id = ''
        for element in state.position:
            state_id += str(element[0])+str(element[1])
        return state_id

    def getSuccessors(self, state):
       successor_list = [];
       for direction in range(len(self.direction)):
           for obj in range(self.num_objs):
                successor = self.move(state, direction, obj)
                if successor:
                    successor_list.append([successor, state, direction, obj, self.getNodeID(successor)])
       
       return successor_list
       
       
    def move_up(self, obj, state, successor):
        
        check = -1
        for i in range(self.num_objs):
            if state.position[obj][0] == state.position[i][0] \
                    and state.position[obj][1] == state.position[i][1]+1:
                return []
            elif state.position[obj][0] == state.position[i][0] \
                    and state.position[obj][1] > state.position[i][1]+1:
                if state.position[i][1] > check:
                    check = state.position[i][1]
        if check>-1:
                successor_positions =  [[i,j] for i,j in state.position]
                successor_positions[obj][1] = check+1
                successor = State(successor_positions)
        return successor
        
    def move_down(self, obj, state, successor):
        
        check = 100
        for i in range(self.num_objs):
            if state.position[obj][0] == state.position[i][0] \
                    and state.position[obj][1] == state.position[i][1]-1:
                return []
            elif state.position[obj][0] == state.position[i][0] \
                    and state.position[obj][1] < state.position[i][1]-1:
                if state.position[i][1] < check:
                    check = state.position[i][1]
        if check<100:
                successor_positions =  [[i,j] for i,j in state.position]
                successor_positions[obj][1] = check-1
                successor = State(successor_positions)
        return successor
        
    def move_left(self, obj, state, successor):
        
        check = -1
        for i in range(self.num_objs):
            if state.position[obj][1] == state.position[i][1] \
                    and state.position[obj][0] == state.position[i][0]+1:
                return []
            elif state.position[obj][1] == state.position[i][1] \
                    and state.position[obj][0] > state.position[i][0]+1:
                if state.position[i][0] > check:
                    check = state.position[i][0]
        if check>-1:
                successor_positions =  [[i,j] for i,j in state.position]
                successor_positions[obj][0] = check+1
                successor = State(successor_positions)
        return successor
        
        
    def move_right(self, obj, state, successor):
        
        check = 100
        for i in range(self.num_objs):
            if state.position[obj][1] == state.position[i][1] \
                    and state.position[obj][0] == state.position[i][0]-1:
                return []
            elif state.position[obj][1] == state.position[i][1] \
                    and state.position[obj][0] < state.position[i][0]-1:
                if state.position[i][0] < check:
                    check = state.position[i][0]
        if check<100:
                successor_positions =  [[i,j] for i,j in state.position]
                successor_positions[obj][0] = check-1
                successor = State(successor_positions)
        return successor


    def move(self, state, direction, obj):
        successor = []
        if direction == 0:      # MOVE UP
            successor = self.move_up(obj, state, successor)
            return successor

        if direction == 1:      # MOVE DOWN
            successor = self.move_down(obj, state, successor)
            return successor

        if direction == 2:      # MOVE LEFT
            successor = self.move_left(obj, state, successor)
            return successor

        if direction == 3:      # MOVE RIGHT
            successor = self.move_right(obj, state, successor)
            return successor


    def state_grid(self, state):
       show_grid = [['*' for i in range(5)] for j in range(5)]
       for i in range(len(state.position)):
           show_grid[state.position[i][1]][state.position[i][0]] = self.labels[i];
       show_grid = np.array(show_grid)
       print show_grid




