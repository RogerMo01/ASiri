import pandas as pd
from src.gemini import Gemini
from src.data_access_prompts import *
from src.utils import format_python_code, add_task_to_csv, delete_task_from_csv

llm = Gemini()
df = pd.read_csv('tasks.csv')

# Start info prompt
info_prompt = info_df(df)


def Get(question: str):

    extract_date_prompt = extract_date(question)
    extracted_date = llm(extract_date_prompt)
    count = 0
    while extracted_date == "No date found":
        extracted_date = llm(extract_date_prompt)
        count+=1
        if count == 3:
            break
    # Maybe there are cases where there is no date then 
    print(f"GET: The extracted_date is -> {extracted_date}")
    query_prompt = get_query(question, extracted_date)
    code = llm(info_prompt + query_prompt)

    code = format_python_code(code)
    print(f"GET: The code is -> {code}")
    try:
        response = eval(code)
    except:
        count = 0
        while True:
            try:
                code = llm(info_prompt + query_prompt)
                response = eval(code)
                break
            except:
                count+=1
                if count == 3:
                    response = "I couldn't do what you asked me to do."
                    break
    return response


def Post(question: str):
    global df
    extract_action_prompt = extract_action(question)   # always there is an action
    task_action = llm(extract_action_prompt)
    count = 0
    while task_action == "No task":
        task_action = llm(extract_action_prompt)
        if count == 3:
            break
    
    print(f"POST: The task_action is -> {task_action}")

    extract_date_prompt = extract_date(question)
    date = llm(extract_date_prompt)
    count = 0
    while date == "No date found":
        date = llm(extract_date_prompt)
        count+=1
        if count == 3:
            break
    print(f"POST: The extracted_date is -> {date}")

    similarity_prompt = check_task_equivalence(task_action, date, df['Task_Name'], df['Date'])
    similarity = None
    count = 0
    yes_counter = 0
    no_counter = 0
    # let it think (3 times)
    while count < 3:
        similarity = llm(similarity_prompt)
        if similarity == 'yes': yes_counter+=1
        else: no_counter+=1
        count+=1

    similarity = 'yes' if yes_counter > no_counter else "no"

    print(f"POST: similarity is -> {similarity}")

    if similarity == 'yes':
         response = "The task is already scheduled."
    else:
            df = add_task_to_csv(df, task_action, date)
            response = "Tasks added successfully."        
    return response


def Remove(question: str):
    global df
    task_prompt = extract_task(question,df['Task_Name'], df['Date'])
    task = llm(task_prompt)
    count = 0
    while task == 'No task':
        task = llm(task_prompt)
        count+=1
        if count == 3:
            if task == 'No task':
                task = None
            break
    print(f'REMOVE: The extracted task is -> {task}')
    
    count = 0
    
    date_prompt = extract_date(question)
    date = llm(date_prompt)
    while date == 'No date found':
        date = llm(date_prompt)
        count+=1
        if count == 3:
            if date == "No date found":
                date = None
            break
    print(f'REMOVE: The extracted date is -> {date}')
    
    if task == None and date == None:
        response = "Something is wrong, I remove by task or by date, and these hasn't provided"
        return response

    # code = llm(info_prompt + query_prompt)
    # code = format_python_code(code)
    df = delete_task_from_csv(df, task, date)
    df.to_csv('tasks.csv', index=False)
    response = "The task was removed"
    return response
