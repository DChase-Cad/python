from time import sleep

wizard = {
    'name': 'Wizard',
    'hp': 70,
    'damage': 150,
    'killMessage': 'decimates the dragon with masterful use of the arcane.',
    'damageType': 'magic'
}
elf = {
    'name': 'Elf',
    'hp': 100,
    'damage': 100,
    'killMessage': 'aims carefully, and with the skill of a master marksman, fells the dragon with shots aimed true.',
    'damageType': 'piercing'
}
human = {
    'name': 'Human',
    'hp': 150,
    'damage': 20,
    'killMessage': 'slays the dragon through sheer will and unwavering bravery, with a mighty blow of the sword.',
    'damageType': 'bludgeoning'
}

dragon = {
    'name': 'Dragon',
    'hp': 300,
    'damage': 50,
    'killMessage': 'into a pile of soot and ash, and lives to kill another day.',
    'damageType': 'slashing and fire'
}

orc = {
    'name': 'Orc',
    'hp': 300,
    'damage': 51,
    'killMessage': "arcs their axe with the force of their ancestors behind them, and the dragon's head is parted from its body.",
    'damageType': 'slashing'
}


# function to simulate the fight
def fight(player, char):
    playerDamage = char["damage"]
    playerHp = char["hp"]
    enemyDamage = dragon['damage']
    enemyHp = dragon['hp']

    while True:
        enemyHp -= playerDamage
        print(
            f'\n{player} damaged the dragon for {playerDamage} {char["damageType"]} damage!')
        print(f'The dragon has {enemyHp} remaining health.')
        sleep(2.5)
        if enemyHp <= 0:
            print(f'\n{player} {char["killMessage"]}')
            break

        playerHp -= enemyDamage
        print(
            f'\nThe dragon attacks {player} for {enemyDamage} {dragon["damageType"]} damage!')
        print(f'{player} has {playerHp} remaining health.')
        sleep(2.5)
        if playerHp <= 0:
            print(f'\nThe dragon torches {player} {dragon["killMessage"]}')
            break


# function to input a non empty character name
def nameChar(character):
    while True and character != '5' and character != 'exit':
        playerName = input(
            f'Please enter the name of your {character["name"].lower()}: ')
        playerName = playerName.capitalize()
        if playerName != '':
            break
        else:
            print("Please enter a name!")
    return playerName


def startGame():
    print('Here are the following heroes of Exandria:')
    print('1)   Wizard')
    print('2)   Elf')
    print('3)   Human')
    print('4)   Orc')
    print('5)   Exit the Game')
    character = input("Enter your choice of character or exit the game:")
    return character.lower()
