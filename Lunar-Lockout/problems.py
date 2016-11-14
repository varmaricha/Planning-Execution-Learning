# -*- coding: utf-8 -*-
"""
Created on Sun Oct 09 13:35:25 2016

@author: richa_000
"""

class Problems(object):
# PROBLEM FILE 
#self.labels = ['r','g','o','p','y','b']
    def __init__(self):
        self.init_state_vector = [0]*4
        self.goal_state = [2,2]
        self.init_state_vector[0] = [(2,0),(2,2),(4,0),(1,3),(3,4)]  # 9
        self.init_state_vector[1] = [(2,0),(2,4),(0,4),(4,4)] # 18
        self.init_state_vector[2] = [(4,4),(4,0),(1,0),(0,2),(3,2),(0,4)] # 27
        self.init_state_vector[3] = [(2,0),(4,1),(0,1),(0,3),(4,3),(2,4)] # 36
        self.problem_map = [9, 18, 27, 36]



    
