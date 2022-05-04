from BonusTask import BonusTask
from QuickTask import QuickTasks


class Gameplay:

    def __init__(self):
        self.first_player_choice = ['up', 'down', 'left', 'right']
        self.second_player_choice = ['left', 'right']

        self.caste_choice = QuickTasks(
            message="The castle gate is closed you can DESTROY it or LOOK for another entrance",
            choices={'destroy': "The king has ordered you to hang",
                     'look': "Good move, You're find open gate"})

        self.cave_choice = QuickTasks(
            message="You have met a dragon, you can fight witch him or escape to other cave." + "What do you choose?" +
                    "\nFIGHT or ESCAPE",
            choices={'fight': "You've been eaten",
                     'escape': "You're lucky man, You're find treasure." +
                               "\nNow you can go LEFT or RIGHT, What do you choose?"})

        self.food_choice = QuickTasks(
            message="Well done you found Wild Blueberries, what do you do now?" + "\nEAT it or DROP it",
            choices={'eat': "You are poisoned, you lose half HP",
                     'drop': "This wild blueberries aren't great to eat, good to you to not eat it"})

        self.weapon_choice = QuickTasks(
            message="It's impossible, You find Iconic Sword stucked in rock. What're you doing with that find?" +
                    "\nPICK or LEAVE",
            choices={'pick': "It's a sword called Aerondight, by pulling it out of the rock you became the new King",
                     'leave': "You will forever be just a Knight"})

        self.fell_from_height = BonusTask(
            message="You fell from a great height and you died")

        self.survive = BonusTask(
            message="You've made it, you've survived")

    def player_choice(self):
        self.starter_question(message="\nYou can go up, down, left or right, where're you go?" + "(u, d ,l or r)")

    def starter_question(self, message: str) -> None:
        print(message)
        self.first_player_choice = input(">>>: ").lower()

    def bonus_question(self, message: str) -> None:
        print(message)
        self.second_player_choice = input(">>>: ").lower()

    def check_player_choice(self) -> None:
        if "u" in self.first_player_choice:
            # if player typed "up" or "u", lead him to the Castle
            self.caste_choice.print_next_quest()
        elif "d" in self.first_player_choice:
            # if player typed "down" or "d", lead him to the Cave
            self.cave_choice.print_next_quest()
            self.bonus_question(message="\nWhere're you go? LEFT or RIGHT")
            if "l" in self.second_player_choice:
                # if player typed "left" or "l", lead him to fell from height
                self.fell_from_height.print_bonus_quest()
                self.bad_ending()
            elif "r" in self.second_player_choice:
                # if player typed "right" or "r", lead him to survive
                self.survive.print_bonus_quest()
                self.good_ending()
        elif "l" in self.first_player_choice:
            # if player typed "left" or "l", lead him to find some food
            self.food_choice.print_next_quest()
        elif "r" in self.first_player_choice:
            # if player typed "right" or "r", lead him to find weapon
            self.weapon_choice.print_next_quest()
            if "p" in self.weapon_choice.choices:
                return self.good_ending()
            else:
                return self.bad_ending()
        else:
            # else call Game Over function
            self.bad_ending()

    @staticmethod
    def good_ending() -> None:
        print("Congratulations, You're win the game")

    @staticmethod
    def bad_ending() -> None:
        print("You're a moron, go to school to learn how to play in this game.")

    def run_game(self) -> None:
        pass
