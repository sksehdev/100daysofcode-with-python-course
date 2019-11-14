import random
from player_rolls import Roll, Player
import logbook
import sys
#level = logbook.DEBUG
game_logger = logbook.Logger("GAME")
#logbook.StreamHandler(sys.stdout, level=level).push_application()

def print_header():
    print('---------------------------------')
    print('          Rock -- Paper -- Scissors')
    print('---------------------------------')
    print()


def build_the_three_rolls():
    return ["Rock", "Paper", "Scissors"]


def get_player_name():
    name = input("Please enter your name :")
    game_logger.debug(f"User entered the name  {name}")
    return name


def game_loop(p1, p2, rolls):
    count = 0
    p1_count = 0
    p2_count = 0
    while count < 3:
        computer_roll = random.choice(rolls)
        game_logger.debug(f"Computer made a random choice {computer_roll}")
        # print(computer_roll)
        p2_roll = p2.player_roll(computer_roll)
        game_logger.info("Computer rolled")
        roll = input('What do you want to roll ? : ')
        while True:
            if roll in rolls:
                p1_roll = p1.player_roll(roll)
                game_logger.info("Player rolled")
                game_logger.debug("Played rolled {}".format(roll))
                break
            else:
                game_logger.info("Played did wrong roll")
                game_logger.debug("Played rolled {}".format(roll))
                roll = input('Wrong Roll.Please Roll again ? : ')

        game_logger.debug(f"{p1.name} rolled {p1_roll.roll_name}")
        game_logger.debug("{} rolled {}".format(p1.name, p1_roll.roll_name))

        outcome = p1_roll.can_defeat(p2_roll)
        if outcome is not None:
            if outcome:
                print(f"{p1.name} won this round")
                p1_count += 1
            else:
                print(f"{p2.name} won this round")
                p2_count += 1
        else:
            p1_count += 1
            p2_count += 1
            print("The round is draw")
        count += 1
    if p1_count < p2_count:
        print(f"{p2.name} won the game")
    elif p1_count == p2_count:
        print("The game is draw")
    else:
        print(f"{p1.name} won the game")


def main():
    print_header()
    name = get_player_name()

    p1 = Player(name)
    p2 = Player("Computer")
    rolls = build_the_three_rolls()

    game_loop(p1, p2, rolls)


def init_logging(filename: str = None):
    level = logbook.DEBUG

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        "stdout mode" if not filename else 'file mode: ' + filename
    )
    logger = logbook.Logger('Startup')
    logger.notice(msg)


if __name__ == '__main__':
    init_logging()
    main()