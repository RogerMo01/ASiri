from datetime import *
from pandas import DataFrame
from src.utils import Conversation

def define_CRUD(text: str) -> str:
    prompt = f"""
You are a personal assistant named Asiri and the person you assist gives you a request of some kind,
the request is: {text}

Analyzing the request given by the person, you have to determine if it is a request to schedule a task,
remove a scheduled task, or asking about a task.

In the case of scheduling a task, respond with: 'POST'.
In the case of removing a scheduled task, respond with: 'REMOVE'.
In the case of asking about a task, respond with: 'GET'.

Examples:
Example 1:
Request: Schedule my friend's wedding for Saturday at 9
Response: 'POST'

Example 2:
Request: Remove the meeting on Saturday at 11 from the schedule
Response: 'REMOVE'

Example 3:
Request: What do I have to do on Friday?
Response: 'GET'

Example 4:
Request: What's on my agenda for today?
Response: 'GET'
"""
    return prompt


def interpret_results(question: str, results):
    response = f"""
You are a task planner assistant. This is the question that the user ask to you:
Question: {question}
and you have generate a response in natural language based in the next results 
obtained from a DataFrame from tasks database
Results: {results.to_markdown() if isinstance(results, DataFrame) else results}
"""
    return response



def use_db(question: str):
    today = datetime.today().strftime('%Y-%m-%d')
    time = datetime.now().time()
    prompt = f"""
You are a task planner assistant with a database of the user tasks. Given a user query, 
you have to determinate if the query needs to be satisfied using the database information,
or the query can be satisfied just using information, that you can provide as a LLM.

Today is: {today}
Current time is: {time}

If query needs tasks database access, your response must be: DB
If query can be answered with LLM, your response must be: NO_DB

Examples:
1) User query: Can you tell me what time is it?
Your response: NO_DB
2) User query: Do I have any plans for today?
Your response: DB
3) User query: Who is Cris Martin?
Your response: NO_DB
4) User query: Add Go to a meeting this sunday
Your response: DB
5) User query: Clear all my plans this week
Your response: DB

Now this is the User Query: {question}
    """
    return prompt




def no_db_response(query: str):
    today = datetime.today().strftime('%Y-%m-%d')
    time = datetime.now().time()
    prompt = f"""
You are a personal task organizer assistant. Your client has made a request, 
and you must respond based on your knowledge as an assistant with an integrated language model. 
Additionally, you are aware of the current day and time. Keep in mind that your capabilities 
as an assistant are those of a language model.

Today is: {today}
Current time is: {time}

Now, the user's request is: {query}
    """
    return prompt


def talk(query: str):
    prompt = f"""
    You are a personal assistant named Asiri. The person you are assisting will give you a task they want you to schedule. This is the task: {query}

    You must determine if the task the user wants to save is an atomic task. You will do this by asking the user something, either a not-so-basic requirement but important for that task.

    Here are some examples:

    Example 1:
    Request: Schedule going to a friend's wedding on Saturday
    Response: Do you have a suit?

    Example 2:
    Request: Save request passport renewal on Monday
    Response: Do you have passport photos?

    Example 3:
    Request: Add business trip to New York on October 15
    Response: Have you booked a hotel in New York?

    Example 4:
    Request: Save a date with my partner on the 14th
    Response: None

    You have an only chance to make a question, so take sure to ask the most important thing for the task.
    Keep in mind that not all tasks require a question. Some can be atomic and simply not require anything else. In such a case, respond with: None in string format.
    Don't make questions about time, just questions that implies do some special task (action no basic) for the person.

"""
    return prompt

def split_task(task: str, conversation:Conversation):
    today = datetime.today().strftime('%Y-%m-%d')
    prompt = f"""
    You are a personal assistant named Asiri. The person you are assisting wants to schedule the following task: {task}. Additionally, you have the following dialogue with them that may provide more context on what they might need: \n
    {conversation}. 
    It is known that today's date is: {today}.

    Now, using all the context, you must take the given task and return, based on the user's needs according to the conversation, a list of possible tasks they need to complete. These tasks should not be basic; they should involve additional work, such as going somewhere or doing something that requires effort. The response should be in the following format:
    Response: [Task1_with_date, Task2_with_date"]

    Example 1:
    Task: Schedule going to a friend's wedding on Saturday
    Conversation:
        Asiri says: Do you have a suit?
        Person says: No
        Asiri says: Then you need to buy one
    Response: [Add buy a suit on Friday, Add go to a friend's wedding on Saturday]

    Example 2:
    Task: Save request passport renewal on Monday
    Conversation:
        Asiri says: Do you have passport photos?
        Person says: No
        Asiri says: Then you need to take new photos
    Response: [Add take passport photos on Sunday, Add request passport renewal on Monday]
    
    Example 3:
    Task: Add business trip to New York on October 15
    Conversation:
        Asiri says: Have you booked a hotel in New York?
        Person says: No
        Asiri says: Then you need to book one
    Response: [Add book a hotel in New York today, Add business trip to New York on October 15]

    Don't split the task into more than two taks, and a task can't be anything that has to do with answering a question to you.
    It's important that the tasks are related to the main task and are related to the conversation.
    The tasks in the array must be related to the main task and the need that arises from the conversation.
"""
    return prompt

def is_atomic_task(conversations):
    prompt = f"""
    You are a personal assistant named Asiri. The person you are assisting has been talking to you about a task they want to schedule. 
    You have been given the following conversation to help you determine if the task is atomic or not: 
    {conversations}.

    That the task is atomic implies that given the conversation has not arisen in addition to the main task another task dibod to some lack or need of the user.

    
    If the task is atomic, respond with: True
    If the task is not atomic, respond with: False
    """
    return prompt

