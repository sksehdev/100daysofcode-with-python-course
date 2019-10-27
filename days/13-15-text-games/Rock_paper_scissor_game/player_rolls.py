class Roll:

    def __init__(self, roll_name):
        self.roll_name = roll_name


    def can_defeat(self, opponent_roll):
        self.opponent = opponent_roll.roll_name
        if self.roll_name == "Rock" and self.opponent == "Paper":
            print("{} will be defeated by {}".format(self.roll_name, self.opponent))
            return False
        if self.roll_name == "Rock" and self.opponent == "Scissors":
            print("{} will defeat the {}".format(self.roll_name, self.opponent))
            return True
        if self.roll_name == "Paper" and self.opponent == "Scissors":
            print("{} will be defeated by {}".format(self.roll_name, self.opponent))
            return False
        if self.roll_name == "Paper" and self.opponent == "Rock":
            print("{} will defeat the {}".format(self.roll_name, self.opponent))
            return True
        if self.roll_name == "Paper" and self.opponent == "Rock":
            print("{} will defeat the {}".format(self.roll_name, self.opponent))
            return True
        if self.roll_name == "Scissors" and self.opponent == "Rock":
            print("{} will be defeated by {}".format(self.roll_name, self.opponent))
            return False
        if self.roll_name == "Scissors" and self.opponent == "Paper":
            print("{} will defeat the {}".format(self.roll_name, self.opponent))
            return True
        if self.roll_name == self.opponent:
            return None

class Player:

    def __init__(self, name):
        self.name = name

    def player_roll(self, roll_name):
        self.roll = Roll(roll_name)
        return self.roll



