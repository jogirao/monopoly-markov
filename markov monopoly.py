# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:51:46 2020

@author: joaom
"""
    
import numpy as np

prob_dict={3:0.05555555555555555, 
           4:0.05555555555555555, 
           5:0.1111111111111111, 
           6:0.1111111111111111, 
           7:0.16666666666666669, 
           8:0.1111111111111111, 
           9:0.1111111111111111, 
           10:0.05555555555555555, 
           11:0.05555555555555555}


def get_place(pos, roll):
    # Compute new position on map
    pos+=roll
    if pos==30:
        return 40
    elif pos>39:
        return pos-39
    return pos
   
def comm_chest(pos):
    # Transition probability vector associated to the community chest deck
    base=np.zeros((42,), dtype=int)
    base[0]=1/17
    base[40]=1/17
    base[pos]=15/17
    return base

def chance(pos):
    # Transition probability vector associated to the chance deck
    # Base vector
    base=np.zeros((42,), dtype=int)
    base[0]=1
    base[5]=1
    base[11]=1
    base[24]=1
    base[39]=1
    base[40]=1
    base[pos]=7
    # Conditional entries
    if pos==7:
        base[4]+=1
        base[12]+=1
        base[15]+=1
        return base/16
    elif pos==22:
        base[19]+=1
        base[25]+=1
        base[28]+=1
        return base/16
    else:
        base[5]+=1
        base[12]+=1
        return np.multiply(base/17, comm_chest(pos)) 
   
def moves(pos):
    # Probability of ending in each pos based on the input pos
    base=np.zeros(42)
    for i in range(3,12):
        base[pos+i]=prob_dict(i)
    return base
    
def roll(v=np.zeros(42), pos, nb=1):
    # Update vector with each roll
    for d1 in range(1,7):
        for d2 in range(1,7):
            # Doubles
            if d1==d2:
                if nb<3:
                    """ Missing changes due to special places"""
                    
                    return roll(v, pos+d1+d2, nb+1)
                else:
                    # Triple doubles
                    v[40]+=1/216
                    return v
            else:
                base=moves(pos)
                
                
def get_vector(pos):
    # Compute transition probability vector given position
    counter=np.zeros((42,), dtype=int)
    counter=pos_count(pos, 1, pos==40, counter)
    return prob_vector(counter)
    
def get_trans(state):
    # Compute transition vector p
    return get_vector(state, False)
    
# Compute markov transition matix
P=[] # Transition probability matrix
for state in range(41):
    # Transition vector
    p=get_trans(state)
    # Update transition matrix
    P.append(p)
                