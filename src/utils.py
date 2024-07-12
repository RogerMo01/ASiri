class Task:
    def __init__(self, name, date) -> None:
        self.name = name
        self.date = date


class Conversation:
    def __int__ (self) -> None:
        self.dialogues = []

    def add_dialogue(self,dialoguer, text):
        self.dialogues.append((dialoguer, text))


def format_python_code(code: str):
    """Remove python annotation whit (```)"""
    if code.startswith("```python"):
        code = code[9:]
    if code.endswith("```"):
        code = code[:len(code)-4]
    return code