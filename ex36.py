"""A skyrimsque dungeon"""

minions_killed, boss_killed, money_looted, stuff_taken, potion_taken =\
    False, False, False, False, False
door_locked = True
stairs_found = False
health = 0
facing_towards = 'east'
orientation = {
    'ahead': 'east',
    'left': 'north',
    'right': 'south',
    'back': 'west'
}


def set_defaults():
    global minions_killed, boss_killed, money_looted, stuff_taken, potion_taken, door_locked,\
        stairs_found, health, facing_towards, orientation
    minions_killed, boss_killed, money_looted, stuff_taken, potion_taken = \
        False, False, False, False, False
    door_locked = True
    stairs_found = False
    health = 50
    facing_towards = 'east'
    orientation = {
        'ahead': 'east',
        'left': 'north',
        'right': 'south',
        'back': 'west'
    }


def set_orientation(direction):
    global facing_towards
    facing_towards = orientation[direction]
    if direction == 'left':
        orientation['ahead'], orientation['left'], orientation['back'], orientation['right'] =\
            orientation['left'], orientation['back'], orientation['right'], orientation['ahead']
    elif direction == 'right':
        orientation['ahead'], orientation['left'], orientation['back'], orientation['right'] = \
            orientation['right'], orientation['ahead'], orientation['left'], orientation['back']
    elif direction == 'back':
        orientation['ahead'], orientation['left'], orientation['back'], orientation['right'] = \
            orientation['back'], orientation['right'], orientation['ahead'], orientation['left']
    # print facing_towards, direction, orientation


def get_input(question, valid_values):
    global health
    if health == 0:
        print 'You die.'
        print '.'
        print '.'
        print '.'
        print 'You are awaken from the slumber by the sudden turn of events. You realize you had ' \
              'just fallen asleep. Or did you?'
        set_defaults()
        while main_room():
            pass
    inp = raw_input('\n' + question + ' > ')
    while inp not in valid_values:
        print 'Your valid moves are:\n\t', valid_values
        inp = get_input(question, valid_values)
    return inp


def main_room():
    global boss_killed, money_looted, stuff_taken, potion_taken, health, facing_towards
    print 'You find yourself at the entrance of an ancient room. You remember you had decided to ' \
          'enter it out of curiosity.'
    set_orientation(get_input('Where do you go?', ('left', 'right', 'back', 'ahead')))
    if facing_towards in ('north', 'south'):
        print 'You are blocked by a wall. The wall looks impenetrable.'
        main_room()
    elif facing_towards == 'west':
        if money_looted and stuff_taken and potion_taken:
            print 'You feel accomplished.'
        if boss_killed:
            print 'You won your adversary and you did good.'
            return
        elif health != 50:
            print 'You persevered in the face of stronger enemy today. A day shall come for you' \
                  ' to return and take on what you left behind.'
            return
        else:
            print 'You did not expect this. You prefer more leisurely activities.'
    else:
        print 'You march onwards.'
        tunnel()


def tunnel():
    global facing_towards
    print 'You find yourself in a tunnel. You see it ends in a big room full of darkness.'
    set_orientation(get_input('Where do you go?', ('back', 'ahead')))
    if facing_towards == 'west':
        print 'It looked too daunting. You decide to play safe.'
        main_room()
    else:
        print 'Undaunted, you march onwards.'
        big_room()


def big_room():
    global door_locked, stairs_found, facing_towards
    print 'You are in a big room. Darkness hampers your vision.'
    if facing_towards == 'east':
        print 'You can make out a door in front of you, and a ledge above it.'
    if stairs_found:
        print 'You know where the stairs are.'
    else:
        print 'You wonder if there are any stairs to the ledge.'
    set_orientation(get_input('Where do you go?', ('left', 'right', 'back', 'ahead')))
    if facing_towards == 'north':
        if stairs_found:
            stairs(True)
        else:
            print 'You see stairs going up ahead to the ledge. Hmm...'
            stairs_found = True
            big_room()
    elif facing_towards == 'south':
        money_room()
    elif facing_towards == 'east':
        if door_locked:
            print 'The door is locked from the other side.'
            big_room()
        else:
            print 'The door is unlocked.'
            boss_room()
    else:
        print 'You step backwards.'
        tunnel()


def stairs(go_up):
    print 'You take the stairs.'
    if go_up:
        set_orientation('right')
        ledge()
    else:
        set_orientation('left')
        big_room()


def money_room():
    global money_looted
    print 'You are in a small room. You find an unlocked coffer.'
    if money_looted or money_looted is None:
        print 'You have already taken care of it. There was nothing else to do so you decide to' \
              ' step back.'
        set_orientation('back')
    else:
        print 'Gold shines from inside.'
        inp = get_input('How much do you take from it?', ('all', 'coin', 'nothing'))
        if inp == 'all':
            print 'You could not control your greed. You feel heavy but carry on.'
            money_looted = True
            money_room()
        elif inp == 'coin':
            print 'You take a coin for study. You plan to come back.'
            money_looted = None
            money_room()
        else:
            print 'You do not know who it belongs to. You decide against taking from it.'
            set_orientation('back')
    big_room()


def ledge():
    global stuff_taken, health, facing_towards
    keys = {value: key for key, value in orientation.items() if value == 'north' or value == 'east'}
    for key, value in keys.items():
        if value == 'ahead':
            keys[key] = 'up ahead'
        elif value == 'left' or value == 'right':
            keys[key] = 'to the ' + value
        else:
            keys[key] = 'behind'
    print 'You are now on the ledge. You see a room {0} and a door {1}.'.format(
        keys['north'], keys['east']
    )
    set_orientation(get_input('Where do you go?', ('left', 'right', 'back', 'ahead')))
    if facing_towards == 'east':
        print 'The door leads through a tunnel and opens to a room to the right.'
        set_orientation('right')
        minions_room()
        set_orientation('left')
    elif facing_towards == 'north':
        potions_room()
    elif facing_towards == 'west':
        stairs(False)
    else:
        if stuff_taken:
            print 'There is only empty space. You step back.'
        else:
            print 'You step over a metallic object. It shines sharply and feels pointy.'
            health -= 10
            inp = get_input('What do you do?', ('pick', 'ignore'))
            if inp == 'pick':
                print 'You pick the pointy metallic object. It is an old sword. You keep it.'
                stuff_taken = True
            else:
                print 'It looked too dangerous to touch. You step back.'
        set_orientation('back')
        ledge()


def potions_room():
    global potion_taken
    print 'You are in a small room. You find a stove with boiling hot tea over it. A cup is nearby.'
    if potion_taken:
        print "You know something about what's boiling, and that feels enough. You couldn't " \
              'possibly try drinking it again. You step back.'
    else:
        inp = get_input('What do you do?', ('drink', 'leave'))
        if inp == 'drink':
            print 'You could only take a sip before its repulsive taste told you it is not tea.'
            potion_taken = True
        else:
            print 'You decide not to taste unknown drink. You grow suspicious of recent activity.'
        print 'Quickly, you get out of that room.'
    set_orientation('back')
    ledge()


def minions_room():
    global money_looted, stuff_taken, potion_taken, minions_killed, health, facing_towards
    if minions_killed:
        print 'You are inside another big room. You see the carcasses of 2 people.'
    else:
        print 'You are inside another big room, but it is not empty like others. There are 2 ' \
              'people inside.'
    set_orientation(get_input('Where do you go?', ('back', 'ahead')))
    if facing_towards == 'south':
        if minions_killed:
            boss_room()
        else:
            print 'Both of them look at you with fear and anger.'
            if money_looted:
                print 'You feel un-welcomed in your gut.'
                inp = get_input('What do you do?', ('attack', 'leave'))
            else:
                if money_looted is None:
                    print 'They do not know you carry a coin of theirs, yet.'
                inp = get_input('What do you do?', ('attack', 'leave', 'talk'))
            if inp == 'attack':
                if money_looted:
                    print 'You feel the heaviness of gold. It slows you down.'
                    health -= 10
                if potion_taken:
                    print 'You move fast... very fast... so fast you surprise yourself.'
                    if stuff_taken:
                        print 'You remember your fencing lessons. The sword you picked moves in ' \
                              'your hand without any effort. Before long you emerge a survivor.'
                    else:
                        print 'Your bare hands are an even match for 2 of them. Some bruises are ' \
                              'nothing new for you.'
                        health -= 10
                        print 'You check the pockets of the dead, looking for an id. A piece of ' \
                              'paper comes in your hand on which "WANTED" is printed.'
                    minions_killed = True
                    minions_room()
                else:
                    print 'Your legs disobey you for a moment.'
                    health -= 10
                    if stuff_taken:
                        print 'You fail to make the first move. But there is no other option left' \
                              ' for you. The fight goes on longer than you expected. You survive.' \
                              ' You check the pockets of the dead, looking for an id. A piece of' \
                              ' paper comes in your hand on which "WANTED" is printed.'
                        minions_killed = True
                        minions_room()
                    else:
                        print 'Their eyes are fixated on the coin shining through your pocket. ' \
                              'They move fast. You never had a chance against the two of them.'
                        health = 0
            elif inp == 'leave':
                ledge()
            else:
                print 'Against all odds, you decide to talk to the strangers.\nAgainst your ' \
                      'ideas, they appear friendly.'
                if money_looted:
                    print 'Sadly, they see gold in your pockets. You have no option but to fight.' \
                          '\nYou feel the heaviness of gold.'
                    health -= 10
                    if potion_taken:
                        if stuff_taken:
                            print 'You remember your fencing lessons. The sword you picked moves ' \
                                  'in your hand without any effort. Before long you emerge a ' \
                                  'survivor.'
                        else:
                            print 'Your bare hands are an even match for 2 of them. Some bruises ' \
                                  'are nothing new for you.'
                            health -= 10
                            print 'You check the pockets of the dead, looking for an id. A piece ' \
                                  'of paper comes in your hand on which "WANTED" is printed.'
                    else:
                        print 'Your legs disobey you for a moment.'
                        health -= 10
                        if stuff_taken:
                            print 'You fail to make the first move. But there is no other option ' \
                                  'left for you. The fight goes on longer than you expected. You ' \
                                  'survive. You check the pockets of the dead, looking for an id.' \
                                  ' A piece of paper comes in your hand on which "WANTED" is ' \
                                  'printed.'
                            minions_killed = True
                        else:
                            print 'Their eyes are fixated on the coin shining through your ' \
                                  'pocket. They move fast. You never had a chance against the two' \
                                  ' of them.'
                            health = 0
                else:
                    if money_looted is None:
                        print 'The coin you carry is never revealed in front of them. They tell ' \
                              'you they have a leader. They ask you to meet him.'
                    set_orientation(get_input('What do you do?', ('back', 'ahead')))
                    if facing_towards == 'north':
                        print 'You tell them you feel tired. You say your goodbyes.'
                        ledge()
                    else:
                        print 'They ask you to go ahead.'
                        boss_room()
    else:
        print 'You carefully step back.',
        if not minions_killed:
            print 'They probably did not notice you.'
        ledge()


def boss_room():
    global boss_killed, minions_killed, health, door_locked, facing_towards
    print 'You are inside a room. There is door at one end, almost hidden.'
    if boss_killed:
        print "You see the giant's dead body. You remember the risky encounter with caution."
    elif door_locked:
        print 'A giant sits in front of it. He immediately takes a disliking of you.'
    else:
        print 'The giant ignores you.'
    set_orientation(get_input('What do you do?', ('back', 'ahead', 'left', 'right')))
    if facing_towards == 'north':
        if minions_killed:
            if boss_killed:
                print 'You',
            else:
                print 'Not in mood of another encounter, you',
            print 'trace your way back.'
            minions_room()
        else:
            print 'The door behind you is locked. You cannot go back.'
            boss_room()
    elif facing_towards in ('east', 'south'):
        print 'You are blocked by a wall. You could not possibly go that way.'
        boss_room()
    else:
        if boss_killed:
            print "You step over the giant's body to reach towards the door."
            if door_locked:
                print 'The key unlocks the door.'
                door_locked = False
            else:
                print 'You go ahead through the unlocked door.'
                big_room()
        else:
            if money_looted or money_looted is None:
                print 'The giant is not too fond of the coin in your pocket. The attack is ' \
                      'immediate.'
                health -= 10
                if minions_killed:
                    print 'The rage of giant is 10 folded seeing the fate of his group.'
                    health -= 10
                print 'The fight is tough.',
                if health >= 10:
                    print 'You barely survive.'
                    if door_locked:
                        print 'A key falls from his pocket. You keep it.'
                    boss_killed = True
                else:
                    print 'The giant barely survives.'
                    health = 0
            elif door_locked:
                print 'Your charm wins over the giant. He hands over a key to you to unlock the ' \
                      'door. You unlock the door with it.'
                door_locked = False
            else:
                print 'You go ahead through the unlocked door.'
            big_room()


set_defaults()
main_room()