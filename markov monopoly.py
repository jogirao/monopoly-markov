# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:51:46 2020

@author: joaom
"""
    
import numpy as np

# Get roll probability
Rolls={}
for i in range(1,7):
    for j in range(1,7):
        try:
            Rolls[i+j]+=1/32
        except:
            Rolls[i+j]=1/32

def get_place(pos, roll):
    # Compute new position on map
    pos+=roll
    if pos==30:
        return 40
    elif pos>39:
        return pos-39
    return pos

"""
WRONG: Not considering the cases where the chance or community chest cards alter the position



def pos_count(pos, roll_nb, in_jail, List):
    # Compute position counter
    for r1 in range(1,7):
        for r2 in range(1,7):
            # Doubles
            if r1==r2:
                if roll_nb<3:
                    new_pos=get_place(pos, r1+r2)
                    List[new_pos]+=1
                    List=pos_count(new_pos, roll_nb+1, new_pos==40, List)
                else:
                    List[40]+=1
            # In jail
            elif in_jail:
                List[40]+=1
            # Other situations
            else:
                new_pos=get_place(pos, r1+r2)
                List[new_pos]+=1
                List=pos_count(new_pos, roll_nb+1, new_pos==40, List)
    return List

"""
        
def get_vector(pos):
    # Compute transition probability vector given position
    counter=np.array([0 for i in range(41)])
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
                