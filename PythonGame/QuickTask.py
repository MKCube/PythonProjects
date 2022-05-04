import typing


class QuickTasks:

    def __init__(self, message, choices: typing.Dict[str, str]):
        self.choices = choices
        self.message = message

    def print_next_quest(self) -> None:
        print(self.message)
        choice = input(">>>: ").lower()
        print(self.choices[choice])
