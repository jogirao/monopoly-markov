# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:56:11 2020

@author: joaom
"""

from random import randint

class Monopoly():
    
    def __init__(self, num_players=2):
        self.round=1
        self.turn=0
        self.community=self.get_deck(17)
        self.chance=self.get_(16)
        self.value_map=self.new_Vmap()
        if num_players>8:
            print("Invalid number of players. The maximum number of players allowed is 8. Starting game with 8 players.")
            self.players=self.new_players(8)
        elif num_players<2:
            print("Invalid number of players. The minimum number of players required is 2. Starting game with 2 players.")
            self.players=self.new_players(2)
        else:
            self.players=self.new_players(num_players)
        
    # Generate new players    
    def new_players(self, num_players):
        player_list=[]
        tokens={'Car', 'Battleship', 'Boot', 'Thimble', 'Wheelbarrow', 'Hat', 'Dog', 'Cat'}
        for i in range(num_players):
            player = Game_piece(tokens.pop(randint(0,len(tokens))))
            player_list.append(player)
            
    # Get new deck        
    def get_deck(nb_cards):
        deck=list(range(nb_cards))
        return deck.shuffle()

    # Generate property value map
    def new_Vmap():
        Map= {''}
        
class Property():
    
    def __init__(name, color):
        self.name=name
        self.color=color
        self.houses=0
        self.value=Monopoly.get_prop_value()
        
class Game_piece():
    
    def __init__(self, figure):
        self.money=2
        self.properties=set()
        self.house=0
        self.token=figure
            
        
