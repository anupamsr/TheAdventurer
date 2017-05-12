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

sentences = {
    'question': (
        'Where do you go?',
        'What do you do?',
        'How much do you take from it?'
    ),
    'main_room': (
        'You find yourself at the entrance of an ancient room. You remember you had decided to '
        'enter it out of curiosity.',
        'You are blocked by a wall. The wall looks impenetrable.',
        'You feel accomplished.',
        'You won your adversary and you did good.',
        'You persevered in the face of stronger enemy today. A day shall come for you to return and'
        ' take on what you left behind.',
        'You did not expect this. You prefer more leisurely activities. You stepped out.',
        'You march onwards.'
    ),
    'tunnel': (
        'You find yourself in a tunnel. You see it ends in a big room full of darkness.',
        'It looked too daunting. You decide to play safe.',
        'Undaunted, you march onwards.'
    ),
    'big_room': (
        'You are in a big room. Darkness hampers your vision.',
        'You can make out a door in front of you, and a ledge above it.',
        'You know where the stairs are.',
        'You wonder if there are any stairs to the ledge.',
        'You see stairs going up ahead to the ledge. Hmm...',
        'The door is locked from the other side.',
        'The door is unlocked.',
        'You step backwards.'
    ),
    'stairs': (
        'You take the stairs.',
    ),
    'money_room': (
        'You are in a small room. You find an unlocked coffer.',
        'You have already taken care of it. There was nothing else to do so you decide to step '
        'back.',
        'Gold shines from inside.',
        'You could not control your greed. You feel heavy but carry on.',
        'You take a coin for study. You plan to come back.',
        'You do not know who it belongs to. You decide against taking from it.'
    ),
    'ledge': (
        'You are now on the ledge. You see a room {0} and a door {1}.',
        'The door leads through a tunnel and opens to a room to the right.',
        'There is only empty space. You step back.',
        'You step over a metallic object. It shines sharply and feels pointy.',
        'You pick the pointy metallic object. It is an old sword. You keep it.',
        'It looked too dangerous to touch. You step back.'
    ),
    'potions_room': (
        'You are in a small room. You find a stove with boiling hot tea over it. A cup is nearby.',
        "You know something about what's boiling, and that feels enough. You couldn't possibly try "
        'drinking it again. You step back.',
        'You could only take a sip before its repulsive taste told you it is not tea.',
        'You decide not to taste unknown drink. You grow suspicious of recent activity.',
        'Quickly, you get out of that room.'
    ),
    'minions_room': (
        'You are inside a well-lit room.',
        'You see the carcasses of 2 people.',
        'But it is not empty like others. There are 2 people inside.',
        'Both of them look at you with fear and anger.',
        'You feel un-welcomed in your gut.',
        'They do not know you carry a coin of theirs, yet.',
        'You feel the heaviness of gold. It slows you down.',
        'You start moving fast... very fast... so fast you surprise yourself.',
        'You remember your fencing lessons. The sword you had picked moves in your hand without any'
        ' effort. Before long you emerge a survivor.',
        'Your bare hands are an even match for 2 of them. Some bruises are nothing new for you.',
        'You check the pockets of the dead, looking for an id. A piece of paper comes in your hand '
        'on which "WANTED" is printed.',
        'Your legs disobey you for a moment.',
        'You fail to make the first move. But there is no other option left for you. The fight goes'
        ' on longer than you expected. You survive.',
        'Their eyes are fixated on the coin shining through your pocket. They move fast. You never '
        'had a chance against the two of them.',
        'Against your better decisions, you decide to talk to strangers.\n\tSurprisingly, they '
        'appear friendly.',
        'They see gold in your pockets. Sadly, you have no option but to fight.',
        'The coin you carry is never revealed in front of them.',
        'They tell you they have a leader. They ask you to meet him.',
        'You tell them you feel tired. You say your goodbyes.',
        'They happily take you ahead.',
        'You carefully step back.',
        'They probably did not notice you.'
    ),
    'boss_room': (
        'You are inside a room. There is door at one end, almost hidden.',
        "You see the giant's dead body. You remember the risky encounter with caution.",
        'A giant sits in front of it. He immediately takes a disliking of you.',
        'The giant ignores you.',
        'You trace your way back.',
        'Not in mood of another encounter, you trace your way back.',
        'The door behind you is locked. You cannot go back.',
        'You are blocked by a wall. You could not possibly go that way.',
        "You step over the giant's body to reach towards the door.",
        'The key unlocks the door.',
        'You go ahead through the unlocked door.',
        'The giant is not too fond of the coin in your pocket. The attack is immediate.',
        'The rage of giant is 10 folded knowing the fate of his group.',
        'The fight is tough.',
        'You barely survive.',
        'A key falls from his pocket. You use it to unlock the door.',
        'The giant barely survives.',
        'Your charm wins over the giant. He hands over a key to you to unlock the door. You unlock '
        'the door with it.',
        'You go ahead through the unlocked door.'
    )
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


def get_input(question, valid_values):
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
    print '\n' + question + '\n'
    inp = raw_input('> ')
    while inp not in valid_values:
        print 'Your valid moves are:\n\t', valid_values
        inp = get_input(question, valid_values)
    return inp


def main_room():
    global facing_towards
    print '\n\t' + sentences['main_room'][0]
    set_orientation(get_input(sentences['question'][0], ('left', 'right', 'back', 'ahead')))
    if facing_towards in ('north', 'south'):
        print '\n\t' + sentences['main_room'][1]
        main_room()
    elif facing_towards == 'west':
        if money_looted and stuff_taken and potion_taken:
            print '\n\t' + sentences['main_room'][2]
        if boss_killed:
            print '\n\t' + sentences['main_room'][3]
            return
        elif health != 50:
            print '\n\t' + sentences['main_room'][4]
            return
        else:
            print '\n\t' + sentences['main_room'][5]
    else:
        print '\n\t' + sentences['main_room'][6]
        tunnel()


def tunnel():
    global facing_towards
    print '\n\t' + sentences['tunnel'][0]
    set_orientation(get_input(sentences['question'][0], ('back', 'ahead')))
    if facing_towards == 'west':
        print '\n\t' + sentences['tunnel'][1]
        main_room()
    else:
        print '\n\t' + sentences['tunnel'][2]
        big_room()


def big_room():
    global stairs_found, facing_towards
    print '\n\t' + sentences['big_room'][0]
    if facing_towards == 'east':
        print '\n\t' + sentences['big_room'][1]
    if stairs_found:
        print '\n\t' + sentences['big_room'][2]
    else:
        print '\n\t' + sentences['big_room'][3]
    set_orientation(get_input(sentences['question'][0], ('left', 'right', 'back', 'ahead')))
    if facing_towards == 'north':
        if stairs_found:
            stairs(True)
        else:
            print '\n\t' + sentences['big_room'][4]
            stairs_found = True
            big_room()
    elif facing_towards == 'south':
        money_room()
    elif facing_towards == 'east':
        if door_locked:
            print '\n\t' + sentences['big_room'][5]
            big_room()
        else:
            print '\n\t' + sentences['big_room'][6]
            boss_room()
    else:
        print '\n\t' + sentences['big_room'][7]
        tunnel()


def stairs(go_up):
    print '\n\t' + sentences['stairs'][0]
    if go_up:
        set_orientation('right')
        ledge()
    else:
        set_orientation('left')
        big_room()


def money_room():
    global money_looted
    print '\n\t' + sentences['money_room'][0]
    if money_looted or money_looted is None:
        print '\n\t' + sentences['money_room'][1]
        set_orientation('back')
    else:
        print '\n\t' + sentences['money_room'][2]
        inp = get_input(sentences['question'][2], ('all', 'coin', 'nothing'))
        if inp == 'all':
            print '\n\t' + sentences['money_room'][3]
            money_looted = True
            money_room()
        elif inp == 'coin':
            print '\n\t' + sentences['money_room'][4]
            money_looted = None
            money_room()
        else:
            print '\n\t' + sentences['money_room'][5]
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
    print '\n\t' + sentences['ledge'][0].format(keys['north'], keys['east'])
    set_orientation(get_input(sentences['question'][0], ('left', 'right', 'back', 'ahead')))
    if facing_towards == 'east':
        print '\n\t' + sentences['ledge'][1]
        set_orientation('right')
        minions_room()
    elif facing_towards == 'north':
        potions_room()
    elif facing_towards == 'west':
        stairs(False)
    else:
        if stuff_taken:
            print '\n\t' + sentences['ledge'][2]
        else:
            print '\n\t' + sentences['ledge'][3]
            health -= 10
            inp = get_input(sentences['question'][1], ('pick', 'ignore'))
            if inp == 'pick':
                print '\n\t' + sentences['ledge'][4]
                stuff_taken = True
            else:
                print '\n\t' + sentences['ledge'][5]
        set_orientation('back')
        ledge()


def potions_room():
    global potion_taken
    print '\n\t' + sentences['potions_room'][0]
    if potion_taken:
        print '\n\t' + sentences['potions_room'][1]
    else:
        inp = get_input(sentences['question'][1], ('drink', 'leave'))
        if inp == 'drink':
            print '\n\t' + sentences['potions_room'][2]
            potion_taken = True
        else:
            print '\n\t' + sentences['potions_room'][3]
        print '\n\t' + sentences['potions_room'][4]
    set_orientation('back')
    ledge()


def minions_room():
    global minions_killed, health, facing_towards
    if minions_killed:
        print '\n\t' + '\n\t'.join((sentences['minions_room'][0], sentences['minions_room'][1]))
    else:
        print '\n\t' + '\n\t'.join((sentences['minions_room'][0], sentences['minions_room'][2]))
    set_orientation(get_input(sentences['question'][0], ('back', 'ahead')))
    if facing_towards == 'south':
        if minions_killed:
            boss_room()
        else:
            print '\n\t' + sentences['minions_room'][3]
            if money_looted:
                print '\n\t' + sentences['minions_room'][4]
                inp = get_input(sentences['question'][1], ('attack', 'leave'))
            else:
                if money_looted is None:
                    print '\n\t' + sentences['minions_room'][5]
                inp = get_input(sentences['question'][1], ('attack', 'leave', 'talk'))
            if inp == 'attack':
                if money_looted:
                    print '\n\t' + sentences['minions_room'][6]
                    health -= 10
                if potion_taken:
                    print '\n\t' + sentences['minions_room'][7]
                    if stuff_taken:
                        print '\n\t' + sentences['minions_room'][8]
                    else:
                        print '\n\t' + '\n\t'.join((sentences['minions_room'][9],
                                                    sentences['minions_room'][10]))
                        health -= 10
                    minions_killed = True
                    minions_room()
                else:
                    print '\n\t' + sentences['minions_room'][11]
                    health -= 10
                    if stuff_taken:
                        print '\n\t' + '\n\t'.join((sentences['minions_room'][12],
                                                    sentences['minions_room'][10]))
                        minions_killed = True
                        minions_room()
                    else:
                        print sentences['minions_room'][13]
                        health = 0
            elif inp == 'leave':
                set_orientation('right')
                ledge()
            else:
                print '\n\t' + sentences['minions_room'][14]
                if money_looted:
                    print '\n\t' + '\n\t'.join((sentences['minions_room'][15],
                                                sentences['minions_room'][6]))
                    health -= 10
                    if potion_taken:
                        if stuff_taken:
                            print '\n\t' + sentences['minions_room'][8]
                        else:
                            print '\n\t' + '\n\t'.join((sentences['minions_room'][9],
                                                        sentences['minions_room'][10]))
                            health -= 10
                    else:
                        print '\n\t' + sentences['minions_room'][11]
                        health -= 10
                        if stuff_taken:
                            print '\n\t' + '\n\t'.join((sentences['minions_room'][12],
                                                        sentences['minions_room'][10]))
                            minions_killed = True
                        else:
                            print sentences['minions_room'][13]
                            health = 0
                else:
                    if money_looted is None:
                        print '\n\t' + sentences['minions_room'][16]
                    print '\n\t' + sentences['minions_room'][17]
                    set_orientation(get_input(sentences['question'][1], ('back', 'ahead')))
                    if facing_towards == 'north':
                        print '\n\t' + sentences['minions_room'][18]
                        set_orientation('left')
                        ledge()
                    else:
                        print '\n\t' + sentences['minions_room'][19]
                        boss_room()
    else:
        print '\n\t' + sentences['minions_room'][20],
        if not minions_killed:
            print '\n\t' + sentences['minions_room'][21]
        set_orientation('left')
        ledge()


def boss_room():
    global boss_killed, health, door_locked, facing_towards
    print '\n\t' + sentences['boss_room'][0]
    if boss_killed:
        print '\n\t' + sentences['boss_room'][1]
    elif door_locked:
        print '\n\t' + sentences['boss_room'][2]
    else:
        print '\n\t' + sentences['boss_room'][3]
    set_orientation(get_input(sentences['question'][1], ('back', 'ahead', 'left', 'right')))
    if facing_towards == 'north':
        if minions_killed:
            if boss_killed:
                print '\n\t' + sentences['boss_room'][4]
            else:
                print '\n\t' + sentences['boss_room'][5]
            minions_room()
        else:
            print '\n\t' + sentences['boss_room'][6]
            boss_room()
    elif facing_towards in ('east', 'south'):
        print '\n\t' + sentences['boss_room'][7]
        boss_room()
    else:
        if boss_killed:
            print '\n\t' + sentences['boss_room'][8]
            if door_locked:
                print '\n\t' + sentences['boss_room'][9]
                door_locked = False
            else:
                print '\n\t' + sentences['boss_room'][10]
                big_room()
        else:
            if money_looted or money_looted is None:
                print '\n\t' + sentences['boss_room'][11]
                health -= 10
                if minions_killed:
                    print '\n\t' + sentences['boss_room'][12]
                    health -= 10
                print '\n\t' + sentences['boss_room'][13],
                if health >= 10:
                    print '\n\t' + sentences['boss_room'][14]
                    if door_locked:
                        print '\n\t' + sentences['boss_room'][15]
                    boss_killed = True
                    door_locked = False
                else:
                    print '\n\t' + sentences['boss_room'][16]
                    health = 0
            elif door_locked:
                print '\n\t' + sentences['boss_room'][17]
                door_locked = False
            else:
                print '\n\t' + sentences['boss_room'][18]
            big_room()

print '\n'
print '                       +-+-+-+'
print '            T h e   A d v e n t u r e r'
print '                       +0+0+0+'
print '\n'
set_defaults()
main_room()
