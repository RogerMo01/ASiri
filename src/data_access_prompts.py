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


def get_query(question: str, date):
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

4) question: Get the tasks for January please
   response: df[df['Date'].dt.month == 9]


Now, the question is:
{question}
And the date of the question is {date}
"""
    return query

def extract_task(question: str, task_names):
    task_names_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(task_names)])
    query = f"""

You are a semantic similarity helper. I will provide you with a deletion query and a list of tasks. 
Your job is to determine if any of the tasks in the list have the same meaning than query, in that case you have
to resonse only with the matching task name, just exactly as it appears in the list.
In case any task does not match, your response must be exactly: NO_TASK


Let me show you some examples:

Question is: Delete go to my friend's birthday 
And exists: Go to Pedro's birthday on Monday
Then the answer is: Go to Pedro's birthday on Monday

Question is: Unschedule my today meet.  
And exists: Go to the meeting
Then the answer is: Go to the meeting

Question is: Cancel my date with Benicio.
And exists: Date with Benicio on Thursday
Then the answer is: Date with Benicio on Thursday 

Question is: Delete the task buy dress for the party
And exists: Buy dress for the celebration.
Then the answer is: Buy dress for the celebration


Here are the tasks: 
{task_names_list}

And the query is:
{question}

Note that your answer must be exactly equal to an existing task.
"""
    return query


def remove_query(task: str):
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
{task}
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


# POST
def extract_action(question):
    query = f"""
You are a task extraction assistant. I will provide you with a question or statement, and your job is to extract the main action referred to in the text.

Examples:
1)  question: I need to go shopping on Sunday.
    response: Go shopping

2)  question: Let's organize a meeting for tomorrow.
    response: Organize a meeting

3)  question: Add going to the beach with my friends on August 1st.
    response: Go to the beach

4)  question: Go to dinner with my girlfriend on Sunday.
    response: Go to dinner with my girlfriend    

Now, the question is:
{question}
"""
    return query


def check_task_equivalence(task_action, task_names,date, task_dates):
    task_names_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(task_names)])
    task_dates_list = "\n".join([f"{i+1}. {date}" for i, date in enumerate(task_dates)])
    query = f"""
You are a semantic similarity helper. I will provide you with a task and a list of other tasks. I will also provide you with a date and a list of dates corresponding to the task list. 
Your job is to determine if any of the tasks in the list have the same meaning and date as the task and date provided.

Here is the task: {task_action} 
Here are the other tasks and their corresponding dates: {task_names_list} and {task_dates_list} 
Here is the date: {date} 

Compare the task and date provided with each task and date in the corresponding lists.

Comparison example: - If the task provided is "add a meeting" and the date is "July 14", check if there is a similar task in the task list that matches "meeting with a client" and has the date "2024-07-14".

Make sure to consider synonyms and variations in task wording. For example, "add a meeting" and "meeting with a client" can be considered similar.

Returns "yes" if it finds an exact match on the date and similar task; otherwise, returns "no"
"""
    return query


def extract_date(question):
    today = datetime.today()
    today_str = today.strftime('%Y-%m-%d')
    weekday = today.strftime('%A')

    query = f"""
You are a date extraction wizard. I will provide you with a question that may include a date.
Your task is to extract the specific date mentioned in the question and provide it in the format YYYY-MM-DD.

Here is the context for today's date for reference:
Today's date is {today_str}.

Below is the context of the day of the week for today's date for reference:
Today is {weekday}.

The days of the week are as follows:
- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

Now, extract the date from the following question:

{question}

If the date is mentioned as 'today', return the current date in the format YYYY-MM-DD.
If the date is mentioned as 'tomorrow', return the date in the format YYYY-MM-DD.

If the date is in the format 'August 1', provide the exact date. If the date refers to a day of the week (e.g. 'Saturday'),
return the date corresponding to the next occurrence of that day based on today's date.

For example:
- If today is Monday and the query is "Add to have coffee with my friends on Friday", it returns the exact date of next Friday by calculating it by today's date and day of the week.
- If the query is "Schedule a meeting on Wednesday", it returns the exact date of next Wednesday by calculating it by today's date and day of the week.

Provide the date in the format YYYY-MM-DD. If no specific date is mentioned, respond with 'No date found'.
"""
    return query
