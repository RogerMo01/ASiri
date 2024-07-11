from datetime import datetime
import pandas as pd

def info_df(df):
    info = f"""
You are a data analysis assistant. I will provide you with a
dataset and ask you questions about it.

Here is an brief excerpt of the dataset that you can use
to understand its structure and composition, but the whole
data is much longer.

{df.head().to_markdown()}

The dataset has the following columns.

{df.columns}

The dataset has {len(df)} rows.
"""
    return info


def get_query(question: str):
    today = datetime.today().strftime('%Y-%m-%d')
    query = f"""
Today is {today}, this is usefull if you have to response using dates.

You have to response with panda code, as a single python expresion, 
it must be a single python expresion

Examples:
1) question: Find the maximum value of a column
   response: `df['column_name'].max()`

2) question: Count the different values on some column
   response: `df.groupby('column_name').count()`

3) question: What tasks do I have for today
   response: `df[df['Date'] == {today}]`

Now, the question is:
{question}
"""
    return query

def remove_query(question: str):
    today = datetime.today().strftime('%Y-%m-%d')
    query = f"""
Today is {today}, this is usefull if you have to response using dates.

You have to response with panda code, as a single python expresion, 
it must be a single python expresion

Examples:
1) question: Delete the tasks scheduled for the "some_day", "some_day" is in Year-Month-Day format but in string form.
   response: `df[df['Date'] !='some_day']`

2) question: Remove the appointments from the agenda starting on "some_day", "some_day" is in Year-Month-Day format but in string form.
   response: `df[df['Date'] >= 'some_day']`

3) question: Delete today's tasks
   response: `df[df['Date'] != {today}]`

4) question: Delete "some_task"
   response: `df[df['Task_Name'] != "some_task"]`

Now, the question is:
{question}
"""
    return query


def interpret_results(question: str, results: pd.DataFrame):
    response = f"""
You are a task planner assistant. This is the question that the user ask to you:
Question: {question}
and you have generate a response in natural language based in the next results 
obtained from a DataFrame from tasks database
Results: {results.to_markdown()}
"""
    return response