import pandas as pd
from src.gemini import Gemini
from src.data_access_prompts import *
from src.utils import format_python_code

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
    pass

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

