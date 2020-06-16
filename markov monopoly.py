# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:51:46 2020

@author: joaom
"""
    
import numpy as np

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
        return (base/16 + base[pos]*comm_chest(pos)) 
    
def trigger_pos(pos, nb):
    # Update player's position upon landing on a property
    if pos in [7, 22, 36]:
        base=chance(pos)
    elif pos in [2, 17, 33]:
        base=comm_chest(pos)
    else:
        base=base=np.zeros((42,), dtype=int)
        base[pos]=1
    return base/(36**nb)
    
def roll(v=np.zeros(42), pos, nb=1):
    # Update vector with each roll
    for d1 in range(1,7):
        for d2 in range(1,7):
            # Doubles
            if d1==d2:
                if nb<3:
                    v+=trigger_pos(get_place(pos, d1+d2), nb)
                    """Doesn't update more than one position"""
                    roll(v, pos+d1+d2, nb+1)
                else:
                    # Triple doubles
                    v[40]+=1/46656
            else:
                if pos==40:
                    v[41]+=(1/36**nb)
                else:
                    v+=trigger_pos(get_place(pos, d1+d2), nb)
    return v
                
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
                