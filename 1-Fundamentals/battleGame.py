from resources import *


grammar = 'a'
validCharacter = True


while True:
    character = startGame()
    if character == '5' or character == 'exit':
        print('\nThanks for playing!!!')
        validCharacter = False
        break
    elif character == '1' or character == 'wizard':
        character = wizard
        break
    elif character == '2' or character == 'elf':
        character = elf
        grammar = 'an'
        break
    elif character == '3' or character == 'human':
        character = human
        break
    elif character == '4' or character == 'orc':
        character = orc
        grammar = 'an'
        break
    elif validCharacter:
        print('Invalid character option please try again.')
        sleep(2)
    else:
        break


if validCharacter:
    playerName = nameChar(character)
    print(
        f'\nYou chose {grammar} {character["name"].lower()} named {playerName} as your champion!')
    print(
        f'{playerName} has {character["hp"]}HP and deals {character["damage"]} {character["damageType"]} damage per turn.')
    sleep(5)
    print(
        f'\n\nYou will be fighting a dragon with {dragon["hp"]}HP that deals {dragon["damage"]} combined {dragon["damageType"]} damage per turn!')
    fight(playerName, character)
