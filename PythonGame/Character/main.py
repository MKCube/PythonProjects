from abc import ABC
from typing import List

from Item import Item


class CharacterBase(ABC):

    def __init__(self, name: str, breed: str, hp: int, mp: int, sp: int, sa: bool):
        self.name = name
        self.breed = breed
        self.hp = hp
        self.mp = mp
        self.sp = sp
        self.sa = sa
        self.inventory = []

    def describe_eq(self):
        eq = ""
        for _ in self.inventory:
            eq += _.item() + ", "
        return eq

    def create_items_list(self, items_list: List[Item]):
        self.inventory = items_list[:]

    def who_are_you(self):
        print(f"I'm {self.breed}. My name's {self.name}, I have {self.hp} HealthPoints, {self.mp} ManaPoints, " +
              f"{self.sp} SkillPoints, Did I have SpecialAttributes? {self.sa} , I'm use: {self.describe_eq()}")


class Player(CharacterBase, ABC):
    def __init__(self, name: str, breed: str, hp: int, mp: int, sp: int, sa: bool):
        super().__init__(name, breed, hp, mp, sp, sa)

    class Elf(CharacterBase):
        pass

    class Wizard(CharacterBase):
        pass

    class Creature(CharacterBase):
        pass

    class Man(CharacterBase):
        pass


def main():
    bow = Item("MagicBow", 15, 350000, 50, [70, 20, 5])
    wand = Item("Staff", 10, 8780000, 40, [88, 34, 40])
    hands = Item("Hands", 1, 30, 1, [15, 2, 1])
    sword = Item("Aerondight", 25, 440600, 66, [100, 50, 16])

    legolas = Player.Elf("Legolas", "Elf", 150, 50, 200, True)
    legolas.create_items_list([bow])

    gandalf = Player.Wizard("Gandalf", "Wizard", 100, 250, 100, True)
    gandalf.create_items_list([wand, sword])

    smigol = Player.Creature("Gollum", "Creature", 50, 20, 100, False)
    smigol.create_items_list([hands])

    aragorn = Player.Man("Aragorn", "Man", 170, 15, 300, False)
    aragorn.create_items_list([sword, bow])

    legolas.who_are_you()
    gandalf.who_are_you()
    smigol.who_are_you()
    aragorn.who_are_you()


if __name__ == "__main__":
    main()
