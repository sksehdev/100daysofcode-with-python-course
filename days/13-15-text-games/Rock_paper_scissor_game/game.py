import random
from player_rolls import Roll, Player

def print_header():
    print('---------------------------------')
    print('          Rock -- Paper -- Scissors')
    print('---------------------------------')
    print()


def build_the_three_rolls():
    return ["Rock","Paper", "Scissors"]

def get_player_name():
    name = input("Please enter your name :")
    return name

def game_loop(p1,p2,rolls):
    count = 0
    p1_count = 0
    p2_count = 0
    while count < 3:
        computer_roll = random.choice(rolls)
        # print(computer_roll)
        p2_roll = p2.player_roll(computer_roll)
        roll = input('What do you want to roll ? : ')
        while True:
            if roll in rolls:
                p1_roll = p1.player_roll(roll)
                break
            else:
                print("Wrong roll")
                roll = input('Please Roll again ? : ')


        print("{} rolled {}".format(p1.name, p1_roll.roll_name))
        print("{} rolled {}".format(p2.name, p2_roll.roll_name))

        outcome = p1_roll.can_defeat(p2_roll)
        if outcome is not None:
            if outcome:
                print("{} won this round".format(p1.name))
                p1_count += 1
            else:
                print("{} won this round".format(p2.name))
                p2_count += 1
        else:
            p1_count += 1
            p2_count += 1
            print("The round is draw")
        count += 1
    if p1_count < p2_count:
        print("{} won the game".format(p2.name))
    elif p1_count == p2_count:
        print("The game is draw")
    else:
        print("{} won the game".format(p1.name))


def main():
    print_header()
    name = get_player_name()

    p1 = Player(name)
    p2 = Player("Computer")
    rolls = build_the_three_rolls()

    game_loop(p1,p2,rolls)






if __name__ == '__main__':
    main()