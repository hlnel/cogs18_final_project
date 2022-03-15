"""A collection of function for doing my project."""

class Warrior():
    def __init__(self, name):
        self.strength = 15
        self.dexterity = 5
        self.intelligence = 5
        self.luck = 5
        self.money = 0
        self.weapon = 'sword'
        self.status = 'alive'
        self.name = name
        
class Mage():
    def __init__(self, name):
        self.strength = 5
        self.dexterity = 5
        self.intelligence = 15
        self.luck = 5
        self.money = 0
        self.weapon = 'staff'
        self.status = 'alive'
        self.name = name

class Rogue():
    def __init__(self, name):
        self.strength = 7
        self.dexterity = 7
        self.intelligence = 7
        self.luck = 12
        self.money = 0
        self.weapon = 'blades'
        self.status = 'alive'
        self.name = name
        
class Archer():
    def __init__(self, name):
        self.strength = 5
        self.dexterity = 15
        self.intelligence = 5
        self.luck = 5
        self.money = 0
        self.weapon = 'bow'
        self.status = 'alive'
        self.name = name
        
class Monster():
    
    def __init__(self, name, health=10, status='alive'):
        self.name = name
        self.health = health
        self.status = status
        
def monster_quest():
    """This is the intro to Monster Quest, a choose-your-own-adventure type story told
    through interacting with a ChatBot. Here, the player creates a character and chooses 
    a story quest to take on in order to gain money.
    
    PARAMETERS
    ----------
    none
    
    RETURNS
    -------
    none
    """
    
    # input name to welcome player and introduce them to the premise of the game
    name = input('What\'s your name, traveller?')
    
    print('\nHello there, {}! Welcome to Monster Quest (default mode)!\n'
          'You\'re dirt poor, right now! Broke! Penniless, in fact!\n'
          'The only way this could get worse is if you got yourself in some deep,\n'
          'deep debt but we\'ll be saving that for you at a later time ;)\n'
          'At this moment, you\'ll be picking your class and doing quests,\n'
          'fighting monsters and (hopefully) earning that well-needed bag!\n'
          'How well you do is determined by the stats of your character and\n'
          'your overall luck! It wouldn\'t be any fun otherwise now, would it?\n'.format(name))
    
    # chooses the player's class and provides information about each class and their stats, if needed
    character_class = ''
    
    while character_class != ['warrior', 'mage', 'rogue', 'archer']:
        character_class = input('Now, what would you like your character class to be?\n'
                                'The options are:\n'
                                '- Warrior\n'
                                '- Mage\n'
                                '- Rogue\n'
                                '- Archer\n'
                                'If you\'re confused about each class or would like to know\n'
                                'their detailed stats, type \'help\'.\n')

        if character_class == 'warrior':
            player = Warrior(name=name)
            print('So you\'ve chosen the Warrior class!\n'
                  'The Warrior class is known for their raw strength, boasting a strength stat of 15!\n'
                  'Not too sure what these numbers mean? Don\'t worry, we\'ll teach you more about\n'
                  'what they mean in a bit!')
            break
        elif character_class == 'mage':
            player = Mage(name=name)
            print('So you\'ve chosen the Mage class!\n'
                  'The Mage class is known for their high intelligence, boasting a intelligence stat of 15!\n'
                  'Not too sure what these numbers mean? Don\'t worry, we\'ll teach you more about\n'
                  'what they mean in a bit!')
            break
        elif character_class == 'rogue':
            player = Rogue(name=name)
            print('So you\'ve chosen the Rogue class!\n'
                  'The Rogue class is known for their extreme luck, boasting a luck stat of 12!\n'
                  'Not too sure what these numbers mean? Don\'t worry, we\'ll teach you more about\n'
                  'what they mean in a bit!')
            break
        elif character_class == 'archer':
            player = Archer(name=name)
            print('So you\'ve chosen the Archer class!\n'
                  'The Archer class is known for their great dexterity, boasting a dexterity stat of 15!\n'
                  'Not too sure what these numbers mean? Don\'t worry, we\'ll teach you more about\n'
                  'what they mean in a bit!')
            break
        elif character_class == 'help':
            print('Need some help? Here\'s a description of each class:\n'
                  'WARRIOR:\n'
                  '- A close-range fighter that attacks with their brute strength.\n'
                  '- STR: 15, INT: 5, DEX: 5, LUK: 5\n'
                  'MAGE:\n'
                  '- A long-range fighter that attacks using magic.\n'
                  '- STR: 5, INT: 15, DEX: 5, LUK: 5\n'
                  'ROGUE:\n'
                  '- A close- to mid-range fighter that attacks with knives and stealth.\n'
                  '- STR: 7, INT: 7, DEX: 7, LUK: 12\n'
                  'ARCHER:\n'
                  '- A long-range fighter that attacks with a bow and arrows.\n'
                  '- STR: 15, INT: 5, DEX: 5, LUK: 5\n'
                  'What do these stats mean, you may ask?\n'
                  '- (STR) is a character\'s baseline strength. It characterizes how much damage they\n'
                  'would deal when physically attacking.\n'
                  '- (INT) is a character\'s baseline intelligence. It characterizes the complexity of\n'
                  'any spells they cast. Damage dealt increases with higher complexity spells.\n'
                  '- (DEX) is a characters\'s baseline dexterity. It characterizes how skilled and\n'
                  'accurate they would be in performing precision-based actions.\n'
                  '- (LUK) is a character\'s baseline luck. It characterizes how lucky they would be\n'
                  'in any situation and may grant a small bonus in every action.\n')
        
    # sends the player off to choose their first quest
    adventure_quests(player)
        
def cave(player):
    """This is the Cave Route for Monster Quest.
    
    PARAMETERS
    ----------
    player : Object
        The player Object to be referenced.
    
    RETURNS
    -------
    none
    """
    
    # checks that the character being played is not considered 'dead' before proceeding
    stay = True
    
    while stay != False:
        if player.status == 'dead':
            caught_you = input('Oh no! It seems like the character you\'re trying to\n'
                               'play as is currently not alive!\n'
                               'Would you like to:\n'
                               '- Revive? (BANK) -10\n'
                               '(type \'revive\')\n'
                               '- Create a new character?\n'
                               '(type \'new\')\n'
                               '- Quit?\n'
                               '(type \'quit\')\n')
            if caught_you == 'revive':
                player.money -= 10
                print('You chose to revive yourself.\n'
                      '(BANK) -10\n')
                stay = False
            elif caught_you == 'new':
                monster_quest()
                stay = False
            elif caught_you == 'quit':
                print('Thanks for playing!')
                stay = False
        elif player.status == 'alive':
            break
    
    stay = True
    
    while stay != False:
    # starts off the quest
        entrance = input('You\'ve reached the mouth of the cave. At it\'s entrance, you notice\n'
                         'a decrepit, old sign with a big \'CAUTION\' painted above it.\n'
                         'Do you bother reading it? (yes/no)\n')
        if entrance == 'yes':
            player.intelligence += 2
            print('The sign reads:\n'
                  'CAUTION:\n'
                  'Monsters ahead! If you are reading this, turn back now!!! RUN BOY!!!\n'
                  '\n'
                  'The sign doesn\'t deter you from your current objective but you feel\n'
                  'better prepared for what dangers lay ahead as you enter the cave.\n'
                  '(INT) +2\n')
        elif entrance == 'no':
            print('You already accepted the quest. \'Might as well get it over with,\'\n'
                  'you think as you enter the cave.\n')

        darkness = input('You immediately find yourself awash in completely darkness as you traverse through the cave.\n'
                        'Although you cannot tell where it\'s coming from, you hear hushed whispers and quiet shuffling\n'
                        'that makes your hair raise and keeps your mind wary and alert.\n'
                        'Do you choose to cast a light spell? (yes/no)\n')
        if darkness == 'yes':
            if player.intelligence <= 5:
                player.strength -= 2
                print('You overestimated your magic abilities, only summoning a few pathetic\n'
                      'sparks from your fingertips before they fizzled out completely.\n'
                      'Your revelation is short-lived, however, when you feel something dig its\n'
                      'teeth into your calf.\n'
                      'Blinding waving your weapon, you manage to remove it from your leg before\n'
                      'it could completely take a chunk out but you feel noticeably weaker afterwards.\n'
                      '(STR) -2\n')
            elif player.intelligence < 15:
                print('You summon a small flame in the palm of your hand, providing a bit\n'
                      'of light that barely illuminates enough of the path ahead for you\n'
                      'to forge ahead. You still are able hear faint whispers and noises but\n'
                      'you decide to not pay any heed to it and continue on.\n')
            else:
                encounter = input('You underestimated your magic abilities and accidentally summoned a flame\n'
                                  'akin to a roaring bonfire. The light alerts and wakes up the surrounding\n'
                                  'creatures around you.\n'
                                  'What do you do? (fight/wait/run)\n')
                if encounter == 'fight':
                    player.money += 5
                    print('Taking a closer look, you notive how they seem to be a couple of small fries.\n'
                          'You quickly dispatch of them and loot their belongings.\n'
                          'MONEY +5\n')
                elif encounter == 'wait':
                    player.intelligence += 5
                    print('Willing the flame to weaken, you recognize the creatures as the friendly group\n'
                          'of creatures that you had heard resided in this cave as well. Realizing that you\n'
                          'weren\'t going to be a threat, their stances relaxed and gladly answered any questions\n'
                          'you had about the monster resting deeper inside.\n'
                          'Great thing you waited before doing anything rash to these little guys!\n'
                          '(INT) +5\n')
                elif encounter == 'run':
                    print('In your hurry to back away and flee from these creatures, you stumble\n'
                          'over a rock and impale yourself on a stalagmite.\n')
                    player_death(player)
                    stay = False
                    break

        elif darkness == 'no':
            print('Without the help of any light to guide you, you stumble over\n'
                  'a rock and impale yourself on a stalagmite hidden in the dark.\n')
            player_death(player)
            stay = False
            break

        # creates the monster to be defeated by the player
        cave_spider = Monster(name='Cave Spider')

        boss_fight = input('Turning a corner in what seems like the longest cave system you\'ve ever been\n'
                           'in, you find yourself face-to-face with a hulking mass of coarse, black hair,\n'
                           'ripping apart what seems to be a previous adventurer, if the blood and scraps of\n'
                           'fabric on the floor were any indicator.\n'
                           '\'This must be the cave\'s monster\', you think as you watch the Cave Spider tear\n'
                           'its current victim into pieces before you.\n'
                           'One wrong step and you may be next for lunch! What do you decide to do?\n'
                           '- Fight\n'
                           '- Run\n')
        # confirms that the current input is the first action of the boss fight
        first_choice = True
        while cave_spider.status == 'alive' and player.status == 'alive':
            if boss_fight == 'fight':
                attack = input('You decided to fight it. Would you like to:\n'
                               '- Direct Attack\n'
                               '- Cast Spell\n'
                               '- Shoot Arrow\n')
                if attack == 'direct attack':
                    direct_attack(player=player, target=cave_spider)
                elif attack == 'cast spell':
                    cast_spell(player=player, target=cave_spider)
                elif attack == 'shoot arrow':
                    shoot_arrow(player=player, target=cave_spider)

                # lets the function know that the next input is no longer the first action of the boss fight
                first_choice = False
            elif boss_fight == 'run':
                # customizes the death response depending on the action order of the boss fight
                if first_choice == True:
                    print('In your hurry to back away and flee from the monster, you step on a fragment of your\n'
                          'predecessor\'s bone, the crunch sounding underneath your boot alerting the monster of\n'
                          'your presence. You have but a moment\'s notice before the monster unhinges its jaws and\n'
                          'swallows you whole, too.\n')
                else:
                    print('In your hurry to back away and flee from the monster, you stumble\n'
                          'over a rock and impale yourself on a stalagmite.\n')
                player_death(player)
                stay = False
                break

            if cave_spider.health <= 0:
                cave_spider.status = 'dead'
                break

            # updates the player on the monster's health and prompts their next action
            boss_fight = input('The monster is currently at {} health. Do you wish to:\n'
                               '- Fight\n'
                               '- Run\n'.format(cave_spider.health))

        # updates the monster's status attribute and updates the player's money attribute for quest completion
        if cave_spider.status == 'dead':
            player.money += 25
            print('You defeated the monster!\n'
                  '(BANK) +25\n')

            looting = input('Do you try to loot the monster? (yes/no)\n')

            if looting == 'yes':
                loot(player=player)
            elif looting == 'no':
                pass

            menu(player)
            stay = False
            break

def menu(player):
    """The menu directory for the player to start a new quest, check their
    current stats and money, or to quit the game entirely.
    
    PARAMETERS
    ----------
    player : Object
        The player Class Object to be referenced.
        
    RETURNS
    -------
    outcome : function
        The function to be used after the player has chosen their next option.
    """
    stay = True
    
    while stay != False:
        option = input('MENU:\n'
                       '- Quests\n'
                       '- Current Stats\n'
                       '- Bank\n'
                       '- Quit Game\n')

        if option == 'quests':
            outcome = adventure_quests(player)
            stay = False
        elif option == 'current stats':
            print('Your stats currently are:\n'
                  '(STR): {}\n'
                  '(INT): {}\n'
                  '(DEX): {}\n'
                  '(LUK): {}\n'.format(player.strength, player.intelligence, player.dexterity, player.luck))
            outcome = menu(player)
            stay = False
        elif option == 'bank':
            print('You currently have {} in your bank.'.format(player.money))
            outcome = menu(player)
            stay = False
        elif option == 'quit game':
            outcome = print('Thanks for playing!')
            stay = False
            
    return outcome
        
def adventure_quests(player):
    """Contains the quests available for the player to go on.
    
    PARAMETERS
    ----------
    player : Object
        The player Class Object to be referenced.
        
    RETURNS
    -------
    none
    """
    
    adventure_route = input('Where would you like to go, {}?\n'
                            'Your options are:\n'
                            '- Cave (BOUNTY: 25)\n'.format(player.name))
    if adventure_route == 'Cave' or 'cave':
        cave(player)
        
def player_death(player):
    """Changes the player's status to 'dead' and gives options for what the player can do next.
    
    PARAMETERS
    ----------
    player : Object
        The player Class Object to be referenced.
        
    RETURNS
    -------
    none
    """
    player.status = 'dead'
    
    
    stay = True
    
    while stay != False:
        you_died = input('You died!\n'
                         'Would you like to:\n'
                         '- Restart completely with a new character? (type \'restart\')\n'
                         '- Revive and restart the quest from the beginning? (type \'revive\')\n'
                         '- Quit and exit the game? (type \'quit\')\n'
                         '(disclaimer: reviving will deduct 10 from player\'s bank)\n')
        if you_died == 'restart':
            monster_quest()
            break
        elif you_died == 'revive':
            player.money -= 10
            print('You chose to revive yourself.\n'
                  '(BANK) -10\n')
            player.status = 'alive'
            cave(player)
            break
        elif you_died == 'quit':
            print('Thanks for playing!')
            stay = False
            break
        else:
            pass

def direct_attack(player, target):
    """Determines the strength and power of a direct, physical attack by the player based on their current stats.
    
    PARAMETERS
    ----------
    player : Object
        The player Class Object to be referenced.
    target : Object
        The target that the attack will be directed towards.
        
    RETURNS
    -------
    outcome : string
        String containing the resulting outcome of the attack.
    """
    
    if player.strength <= 5:
        outcome = print('Your {} missed the target.'.format(player.weapon))
    elif player.strength < 15:
        target.health -= 5
        outcome = print('You successfully hit the {} with your {}! The {} lost 5 health points.\n'
                        'It currently has {} health.\n'.format(target.name, player.weapon, target.name, target.health))
    else:
        target.health -= 10
        outcome = print('You struck a powerful blow with your {}! The {} was hit and lost 10 health points.\n'
                        'It currently has {} health.\n'.format(player.weapon, target.name, target.health))
    
    return outcome
            
def cast_spell(player, target):
    """Determines the complexity and success of a spell casted by the player based on their current stats.
    
    PARAMETERS
    ----------
    player : Object
        The player Class Object to be referenced.
    target : Object
        The target that the spell will be directed towards.
        
    RETURNS
    -------
    outcome : string
        String containing the resulting outcome of the cast spell.
    """
    
    if player.intelligence <= 5:
        outcome = print('You failed to cast the spell.')
    elif player.intelligence < 15:
        target.health -= 5
        outcome = print('You succeeded in casting the spell! The {} was hit and lost 5 health points.\n'
                        'It currently has {} health.\n'.format(target.name, target.health))
    else:
        target.health -= 10
        outcome = print('You perfectly cast the spell! The {} was hit and lost 10 health points.\n'
                        'It currently has {} health.\n'.format(target.name, target.health))
    
    return outcome

def shoot_arrow(player, target):
    """Determines the skill and accuracy of an arrow shot by the player based on their current stats.
    
    PARAMETERS
    ----------
    player : Object
        The player Class Object to be referenced.
    target : Object
        The target that the arrow will be shot towards.
        
    RETURNS
    -------
    outcome : string
        String containing the resulting outcome of the shot arrow.
    """
    
    if player.dexterity <= 5:
        outcome = print('You shot the arrow and missed.')
    elif player.dexterity < 15:
        target.health -= 5
        outcome = print('Your arrow made its mark! The {} was hit and lost 5 health points.\n'
                        'It currently has {} health.\n'.format(target.name, target.health))
    else:
        target.health -= 10
        outcome = print('You perfectly shot the arrow, aimed right at the {}\'s weak spot! The {} was hit and lost 10 health points.\n'
                        'It currently has {} health.'.format(target.name, target.name, target.health))
    
    return outcome
            
def loot(player):
    """Determines the loot found by the player based on their current stats
    
    PARAMETERS
    ----------
    player : Object
        The player Class Object to be referenced.
        
    RETURNS
    -------
    outcome : string
        String containing the resulting outcome of the choice to loot.
    """
    
    from random import choice
    
    # lists that the loot will be randomly chosen from using the random.choice() function
    default_loot = ['Gold', 'a Rusty Dagger', 'Bones', 'Wishbone']
    good_loot = ['Gold', 'a Broadsword', 'an Ancient Tome', 'a Claymore', 'a Lucky Clover']
    
    if player.luck <= 5:
        outcome = print('You didn\'t find anything.')
    elif player.luck < 15:
        found_loot = choice(default_loot)
        
        if found_loot == 'Gold':
            player.money += 5
            response = '\n (BANK) +5'
        elif found_loot == 'a Rusty Dagger':
            player.strength += 5
            response = 'You gained 5 strength!\n(STR) +5'
        elif found_loot == 'Bones':
            response = 'They didn\'t do anything.'
        elif found_loot == 'Wishbone':
            player.luck += 2
            response = 'You gained 2 luck!\n(LCK) +2'
        
        outcome = print('You found {}! {}\n'.format(found_loot, response))
    else:
        found_loot = choice(good_loot)
        if found_loot == 'Gold':
            player.money += 10
            response = '\n (BANK) +10'
        elif found_loot == 'a Broadsword':
            player.strength += 10
            response = 'You gained 10 strength!\n(STR) +10'
        elif found_loot == 'an Ancient Tome':
            player.intelligence += 10
            response = 'You gained 10 intelligence!\n(INT) +10'
        elif found_loot == 'a Claymore':
            player.strength += 10
            response = 'You gained 10 strength!\n(STR) +10'
        elif found_loot == 'a Lucky Clover':
            player.luck += 5
            response = 'You became luckier!\n(LUK) +5'
        
        outcome = print('You found {}! {}\n'.format(found_loot, response))
                        
    return outcome