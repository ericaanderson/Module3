# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 20:51:47 2023

@author: erica
"""

import random

class Agent():
    def __init__(self,i):
        """
        The constructor method.
        
         Parameters
        ----------
        i : Integer
            To be unique to each instance.
        
         Returns
        -------
        None.
        
        """
        self.i = i
        self.x = (random.randint(0,99))
        self.y = (random.randint(0,99))
        pass
    
    def __str__(self,i):
        return self.__class__.__name__ + "(x=" + str(self.x) + ", y=" + str(self.y) + ")"
    
    def __repr__(self):
        return str(self)
    
    def move(self, x_min, y_min, x_max, y_max):
        if random.random() < 0.5:
            self.x = self.x +1
        else:
            self.x = self.x -1
   #move y
        if random.random() < 0.5:
            self.y = self.y +1
        else:
            self.y = self.y -1
