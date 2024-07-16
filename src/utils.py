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
        self.dialogues.append((dialoguer, text))

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
        self.dialogues = []

    def is_none(self):
        self.load_dialogues()
        return len(self.dialogues) == 0
    
    def get_first(self):
        if len(self.dialogues)!=0:
            return self.dialogues[0]
        return None


def format_python_code(code: str):
    """Remove python annotation whit (```)"""
    if code.startswith("```python"):
        code = code[9:]
    if code.endswith("```"):
        code = code[:len(code)-4]
    return code

class Crud_flag:

    @staticmethod
    def load_crud_flag() -> str:   # NON_OPER | GET | POST | REMOVE
        with open('crud_flag.txt', 'r') as file:
            crud_flag = file.readline()
        return crud_flag
    
    @staticmethod
    def clean_crud_flag():
        with open('crud_flag.txt', 'w') as file:
            file.write('NON_OPER')

    @staticmethod
    def edit_crud_flag(flag: str):
        with open('crud_flag.txt', 'w') as file:
            file.write('')
            file.write(flag)


# c = Conversation()
# d = [("Pedro","Tienes traje?"),("Juan","Si, tengo"), ("Pedro", "Ah, vale")]
# c.dialogues = d
# c.add_dialogue("Pedro","Hola")

# print(c)
# print(datetime.now().time())

# split_response = '[Buy a suit on Friday, Go to a friend\'s wedding on Saturday]'
# start = split_response.index('[')
# end = split_response.index(']')
# response_array = split_response[start+1:end].split(',')
# print(response_array)

# x = load_crud_flag()
# print(x)

# edit_crud_flag('POST')

# clean_crud_flag()
# x = load_crud_flag()
# print(x)

