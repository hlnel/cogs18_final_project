"""Test for my functions. It was difficult to make asserts since most of my functions
didn't have return or included multiple inputs per function so trying to utilize mock and builtins
was challenging.
"""

from functions import monster_quest, cave, player_death, direct_attack, cast_spell, shoot_arrow, loot, menu, Warrior, Mage, Rogue, Archer, Monster
from random import choice
    
def test_monster_quest():
    assert callable(monster_quest)
    
def test_cave():
    assert callable(cave)
        
def test_direct_attack():
    test_player = Warrior(name='Dummy')
    test_monster = Monster(name='DumbDumb')
    assert direct_attack(player=test_player, target=test_monster) == None
    
def test_cast_spell():
    test_player = Mage(name='Dummy')
    test_monster = Monster(name='DumbDumb')
    assert cast_spell(player=test_player, target=test_monster) == None
    
def test_shoot_arrow():
    test_player = Archer(name='Dummy')
    test_monster = Monster(name='DumbDumb')
    assert shoot_arrow(player=test_player, target=test_monster) == None
    
def test_loot():
    test_player = Rogue(name='Dummy')
    assert loot(player=test_player) == None