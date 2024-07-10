class Task:
    def __init__(self, name, date) -> None:
        self.name = name
        self.date = date


class Conversation:
    def __int__ (self) -> None:
        self.dialogues = []

    def add_dialogue(self,dialoguer, text):
        self.dialogues.append((dialoguer, text))