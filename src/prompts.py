from datetime import *
from pandas import DataFrame


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

If query needs tasks database access, your response must be: `DB`
If query can be answered with LLM, your response must be: `NO_DB`

Examples:
1) User query: Can you tell me what time is it?
Your response: `NO_DB`
2) User query: Do I have any plans for today?
Your response: `DB`
3) User query: Ho is Cris Martin?
Your response: `NO_DB`
4) User query: Add Go to a meeting this sunday
Your response: `DB`
5) User query: Clear all my plans this week
Your response: `DB`

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

# def get_panda_code(text: str, date: datetime, type: str) -> str:
#     prompt = """ 
#     Eres un asistente personal llamado Asiri y la persona a la cual asistes te hace una solicitud, la solicitud es: """+ text+""".

#     Analizando la solicitud que te dio la persona y sabiendo que tienes un .csv llamado tasks.csv y 
#     la fecha de hoy, que es""" + str(date) + """tienes que generar código usando la biblioteca de python pandas,
#       este código debe satisfacer totalmente la solicitud del asistido.

#     Las solicitudes del usuario pueden ser de distinto tipo, el tipo de la solicitud en este caso es: """+type+""".
#     Las solicitudes pueden tener 3 valores diferentes: 'GET', 'POST', 'REMOVE'.
#     Si es 'GET' significa que debes hacer una consulta a tasks.csv usando lo que te dice el usuario.
#     Si es 'POST' significa que debes crear una nueva tarea en tasks.csv usando lo que te dice el usuario.
#     Si es 'REMOVE' significa que debes borrar una tarea de tasks.csv usando lo que te dice el usuario.

#     Ejemplos:

#     Ejemplo 1:
#     Solicitud: Agéndame una reunion con un cliente para el 14 de julio a las 10
#     Explicación: El usuario está pidiendo que se cree una nueva tarea, por tanto es 'POST' la solicitud
#     Respuesta: 

# def agregar_tarea(fecha, descripcion):
#     # Verificar si el archivo CSV existe
#     if os.path.exists('tasks.csv'):
#         # Leer el archivo CSV existente
#         df = pd.read_csv('tasks.csv')
#     else:
#         # Crear un DataFrame vacío con las columnas necesarias
#         df = pd.DataFrame(columns=['Nombre', 'Fecha'])

#     # Crear un nuevo DataFrame con la tarea a agregar
#     nueva_tarea = pd.DataFrame({'Nombre': [nombre], 'Fecha': [fecha]})

#     # Agregar la nueva tarea al DataFrame existente
#     df = pd.concat([df, nueva_tarea], ignore_index=True)

#     # Guardar el DataFrame actualizado en el archivo CSV
#     df.to_csv('tasks.csv', index=False)

# fecha = '2024-07-14'
# nombre = 'Reunion con un cliente'

# agregar_tarea(fecha, nombre)

#     Ejemplo 2:
#     Solicitud: Qué compromisos tengo para el 13 de julio
#     Explicación: El usuario está pidiendo una consulta a la base de datos pasando como filtro cierta fecha, entonces es una solicitud 'GET'.
#     Respuesta:
    
#     def filtrar_tareas(fecha):
#         df = pd.read_csv('tasks.csv')
#         df['Fecha'] = pd.to_datetime(df['Fecha'])
#         fecha = datetime.strptime(fecha, '%Y-%m-%d')
#         tareas_filtradas = df[df['Fecha'] == fecha]
#         return tareas_filtradas

#     fecha = '2024-07-13'
#     tareas_filtradas = filtrar_tareas(fecha)

#     Omite la palabra python al inicio del codigo, devuelve un codigo ejecutable de python, sé cuidadoso con los nombres de las variables fuera de la funciones,
#     deben tener el mismo nombre que se especifica. Tampoco hagas importanciones de ningún tipo, se asume que existe pandas como pd, que tienes la libreria os y que datetime tambien está importada
# """
#     return prompt
