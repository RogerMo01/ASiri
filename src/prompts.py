from datetime import *
def define_CRUD(text: str) -> str:
    prompt = f"""
Eres un asistente personal llamado Asiri y la persona a la cual asistes te hace una solicitud de algún tipo,
la solicitud es: {text}

Analizando la solicitud que te dio la persona tienes que determinar si se trata de una solicitud de agendar una tarea,
eliminar una tarea agendada o te está preguntando por alguna tarea.

Para el caso en que está solicitando una tarea da como respuesta: 'POST'.
Para el caso en que está eliminando una tarea agendada da como respuesta: 'REMOVE'.
Para el caso en que está pidiendo una tarea o preguntando por ella da como respuesta: 'GET'.

Ejemplos:
Ejemplo 1:
Solicitud: Agéndame la boda de mi amigo para el sábado a las 9
Respuesta: 'POST'

Ejemplo 2:
Solicitud: Quita de la agenda la reunión del sábado a las 11
Respuesta: 'REMOVE'

Ejemplo 3:
Solicitud: Qué tengo que hacer el viernes?
Respuesta: 'GET'

Ejemplo 4:
Solicitud: Qué hay en mi agenda para hoy?
Respuesta: 'GET'

"""
    return prompt

def get_panda_code(text: str, date: datetime, type: str) -> str:
    prompt = """ 
    Eres un asistente personal llamado Asiri y la persona a la cual asistes te hace una solicitud, la solicitud es: """+ text+""".

    Analizando la solicitud que te dio la persona y sabiendo que tienes un .csv llamado tasks.csv y 
    la fecha de hoy, que es""" + str(date) + """tienes que generar código usando la biblioteca de python pandas,
      este código debe satisfacer totalmente la solicitud del asistido.

    Las solicitudes del usuario pueden ser de distinto tipo, el tipo de la solicitud en este caso es: """+type+""".
    Las solicitudes pueden tener 3 valores diferentes: 'GET', 'POST', 'REMOVE'.
    Si es 'GET' significa que debes hacer una consulta a tasks.csv usando lo que te dice el usuario.
    Si es 'POST' significa que debes crear una nueva tarea en tasks.csv usando lo que te dice el usuario.
    Si es 'REMOVE' significa que debes borrar una tarea de tasks.csv usando lo que te dice el usuario.

    Ejemplos:

    Ejemplo 1:
    Solicitud: Agéndame una reunion con un cliente para el 14 de julio a las 10
    Explicación: El usuario está pidiendo que se cree una nueva tarea, por tanto es 'POST' la solicitud
    Respuesta: 

def agregar_tarea(fecha, descripcion):
    # Verificar si el archivo CSV existe
    if os.path.exists('tasks.csv'):
        # Leer el archivo CSV existente
        df = pd.read_csv('tasks.csv')
    else:
        # Crear un DataFrame vacío con las columnas necesarias
        df = pd.DataFrame(columns=['Nombre', 'Fecha'])

    # Crear un nuevo DataFrame con la tarea a agregar
    nueva_tarea = pd.DataFrame({'Nombre': [nombre], 'Fecha': [fecha]})

    # Agregar la nueva tarea al DataFrame existente
    df = pd.concat([df, nueva_tarea], ignore_index=True)

    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv('tasks.csv', index=False)

fecha = '2024-07-14'
nombre = 'Reunion con un cliente'

agregar_tarea(fecha, nombre)

    Ejemplo 2:
    Solicitud: Qué compromisos tengo para el 13 de julio
    Explicación: El usuario está pidiendo una consulta a la base de datos pasando como filtro cierta fecha, entonces es una solicitud 'GET'.
    Respuesta:
    
    def filtrar_tareas(fecha):
        df = pd.read_csv('tasks.csv')
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        fecha = datetime.strptime(fecha, '%Y-%m-%d')
        tareas_filtradas = df[df['Fecha'] == fecha]
        return tareas_filtradas

    fecha = '2024-07-13'
    tareas_filtradas = filtrar_tareas(fecha)

    Omite la palabra python al inicio del codigo, devuelve un codigo ejecutable de python, sé cuidadoso con los nombres de las variables fuera de la funciones,
    deben tener el mismo nombre que se especifica. Tampoco hagas importanciones de ningún tipo, se asume que existe pandas como pd, que tienes la libreria os y que datetime tambien está importada
"""
    return prompt
