from datetime import datetime
import pandas as pd
import csv 

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


def add_task_to_csv(df, task, date, filename='tasks.csv'):
    """
    Adds new task to an existing CSV file and updates the DataFrame.
    
    Args:
        df (pandas.DataFrame): The DataFrame containing the tasks.
        filename (str): The name of the CSV file to update.
        
    Returns:
        pandas.DataFrame: The updated DataFrame with the new tasks.
    """
    # # Check if the DataFrame is empty
    # if df.empty:
    #     print("The DataFrame is empty. No tasks to add.")
    #     return df

    # Read the existing content from the CSV file
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        print(f"File {filename} not found. Creating a new file.")
        data = [['Task_Name', 'Date']]  # Create header if file doesn't exist

    # Add new tasks to the list
    new_tasks = [[task, date]]
    data.extend(new_tasks)

    # Write the updated data back to the CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    # Update the DataFrame with the new tasks
    updated_df = pd.read_csv(filename)
    return updated_df




def delete_task_from_csv(df, task, date, filename = 'tasks.csv'):
    date_matter = date is not None
    task_matter = task is not None
    if df.empty:
        print("The DataFrame is empty. No tasks to remove.")
        return df
    try:
        # Leer el archivo CSV existente
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return pd.DataFrame()  # Retornar un DataFrame vacío si no existe el archivo

    # Filtrar las filas que no coincidan con la tarea y la fecha a eliminar
    data_filtered = [row for row in data if not ((task_matter and row[0] == task) and (date_matter and row[1] == date))]

    # Sobrescribir el archivo CSV con los datos filtrados
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_filtered)

    # Actualizar el DataFrame con los datos filtrados
    updated_df = pd.read_csv(filename)
    return updated_df


