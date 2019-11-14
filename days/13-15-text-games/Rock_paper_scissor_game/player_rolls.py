class Roll:

    def __init__(self, roll_name):
        self.roll_name = roll_name
        self.rules = {"Rock": ["Scissors"], "Paper": ["Rock"], "Scissors": ["Paper"]}
        self.opponent = ""

    def can_defeat(self, opponent_roll):
        self.opponent = opponent_roll.roll_name
        if self.roll_name == self.opponent:
            return None
        else:
            return self.opponent in self.rules[self.roll_name]


class Player:

    def __init__(self, name):
        self.name = name

    def player_roll(self, roll_name):
        self.roll = Roll(roll_name)
        return self.roll



