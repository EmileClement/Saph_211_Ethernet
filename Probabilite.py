# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:23:57 2020

@author: Leopold
"""

class Loi():
    def __init__(self, generateur):
        
        self.generateur = generateur
    
    def __call__(self, n):
        X = self.generateur(n)
        return abs(X)
        