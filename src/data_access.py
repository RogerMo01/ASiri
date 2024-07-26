import pandas as pd
from src.gemini import Gemini
from src.data_access_prompts import *
from src.utils import format_python_code, add_task_to_csv

llm = Gemini()
df = pd.read_csv('tasks.csv')

# Start info prompt
info_prompt = info_df(df)


def Get(question: str):
    query_prompt = get_query(question)
    
    code = llm(info_prompt + query_prompt)

    code = format_python_code(code)

    try:
        response = eval(code)
    except:
        response = "I couldn't do what you asked me to do."

    return response

def Post(question: str):
    print(f'Question: {question}')
    # question = question[1]
    global df
    extract_action_prompt = extract_action(question)
    task_action = llm(extract_action_prompt)
    print(f"Extracted Action: {task_action}")  
    extract_date_prompt = extract_date(question)
    date = llm(extract_date_prompt)
    print(f"Extracted Date: {date}")
    similarity_prompt = check_task_equivalence(task_action, date, df['Task_Name'], df['Date'])
    similarity = llm(similarity_prompt)
    print(f"Task Similarity: {similarity}")
    if similarity == 'yes':
         response = "The task is already scheduled."
    else:
        code = format_python_code(task_action)
        df = add_task_to_csv(df, code, date)
        response = "Tasks added successfully."
        
    return response


def Remove(question: str):
    query_prompt = remove_query(question)
    code = llm(info_prompt + query_prompt)

    code = format_python_code(code)
    print(f"THE CODE IS {code}")
    try:
        df = eval(code)
        df.to_csv('tasks.csv', index=False)
        response = "The task was removed"
    except:
        response = "I couldn't do what you asked me to do."

    return response
