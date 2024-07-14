from datetime import datetime
class Task:
    def __init__(self, name, date) -> None:
        self.name = name
        self.date = date


class Conversation:
    
    def __int__ (self):
        self.dialogues = []

    # def add_dialogue(self,dialoguer, text):
        # self.dialogues.append((dialoguer, text))

    def __str__(self) -> str:
        result = ""
        for i in self.dialogues:
            result += f'{i[0]} says: {i[1]}.\n'

        return result 
    
    def add_dialogue(self, dialoguer, text):
        with open('talks.txt', 'a') as archivo:
            archivo.write(f'{dialoguer} says: {text} \n')

    def load_dialogues(self):
        with open('talks.txt', 'r') as file:
            for line in file:
                split_line = line.split(':')
                dialoguer = split_line[0]
                text = split_line[1]
                self.dialogues.append((dialoguer, text)) 

    def clean_dialogues(self):
        with open('talks.txt', 'w') as file:
            file.write('')

    def is_none(self):
        self.load_dialogues()
        return len(self.dialogues) == 0


def format_python_code(code: str):
    """Remove python annotation whit (```)"""
    if code.startswith("```python"):
        code = code[9:]
    if code.endswith("```"):
        code = code[:len(code)-4]
    return code


# c = Conversation()
# d = [("Pedro","Tienes traje?"),("Juan","Si, tengo"), ("Pedro", "Ah, vale")]
# c.dialogues = d
# c.add_dialogue("Pedro","Hola")

# print(c)
# print(datetime.now().time())