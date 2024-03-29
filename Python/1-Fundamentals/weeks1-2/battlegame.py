wizard = 'Wizard'
elf = 'Elf'
human = 'Human'

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

# Dragon - 300 hp and 50 damage.
dragon_hp = 300
dragon_damage = 50

while True:
    print('1. Wizard  2. Elf  3. Human')
    character = input('Choose your character: ')

    if character == '1':
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break

    if character == '2':
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break

    if character == '3':
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break

    print("Invalid selection")

# print character name and data
print(f'You have chosen {character} with HP: {my_hp} and Damage: {my_damage}')

while True:

    dragon_hp -= my_damage
    print('Dragon was attacked, Dragon HP:', dragon_hp)

    if dragon_hp <= 0:
        print('Dragon HP:', dragon_hp)
        print('Dragon lost')
        break

    my_hp -= dragon_damage
    print(f'{character} was attacked, HP: {my_hp}')

    if my_hp <= 0:
        print(f'{character} HP: {my_hp}')
        print(f'{character} lost')
        break

    play_again = input("Do you want to play again? (yes/no): ")
    while play_again.lower() == 'yes':
     # Reset game variables if the player wants to play again

        dragon_hp = 300
    player_hp = 'player_max_hp'
    print("\nStarting a new game!\n")

    play_again = input("Do you want to play again? (yes/no): ")

print("Thank you for playing!")
