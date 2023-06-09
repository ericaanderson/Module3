# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 20:51:47 2023

@author: erica
"""

import random
import my_modules.io as io

class Agent():
    def __init__(self, i, environment, n_rows, n_cols):
        """
        The constructor method.
        
        Parameters
        ----------
        i : Integer
            To be unique to each instance.
        environment : List
            A reference to a shared environment
        n_rows : Integer
            The number of rows in environment.
        n_cols : Integer
            The number of columns in environment.
        
        Returns
        -------
        None.
        
        """
        n_cols = io.n_cols()
        n_rows = io.n_rows()
        
        self.i = i
        self.environment = environment
        tnc = int(n_cols / 3)
        self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        tnr = int(n_rows / 3)
        self.y = random.randint(tnr - 1, (2 * tnr) - 1)

    
    def __str__(self):
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

    def eat(self):
        """
        Eat Method 
        
        Parameters
        ----------
        environment : List
            location value of agent
        >= 10 : value of 'environment' where the agent is located is reduced by 
                10 and added to store
        < 10 :Value of agent location is removed and added to agent store
        self.store: attribute of agent 

        Returns
        -------
        store value

        """
        self.store = 0
        store = []
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            store.append(self.store)
        else:
            self.environment[self.y][self.x] - self.environment[self.y][self.x]
            self.store += self.environment[self.y][self.x]
            store.append(self.store)
        return store


         