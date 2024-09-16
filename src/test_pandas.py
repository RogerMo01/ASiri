import pandas as pd
import os
from datetime import datetime

# def agregar_tarea(nombre_archivo, fecha, hora, descripcion):
#     # Verificar si el archivo CSV existe
#     if os.path.exists(nombre_archivo):
#         # Leer el archivo CSV existente
#         df = pd.read_csv(nombre_archivo)
#     else:
#         # Crear un DataFrame vacío con las columnas necesarias
#         df = pd.DataFrame(columns=['Nombre', 'Fecha'])

#     # Combinar fecha y hora
#     fecha_hora_str = f'{fecha} {hora}'
#     # Convertir a objeto datetime
#     fecha_hora = datetime.strptime(fecha_hora_str, '%Y-%m-%d %H:%M:%S')

#     # Crear un nuevo DataFrame con la tarea a agregar
#     nueva_tarea = pd.DataFrame({'Nombre': [descripcion], 'Fecha': [fecha_hora]})

#     # Agregar la nueva tarea al DataFrame existente
#     df = pd.concat([df, nueva_tarea], ignore_index=True)

#     # Guardar el DataFrame actualizado en el archivo CSV
#     df.to_csv(nombre_archivo, index=False)

# # Ejemplo de uso
# nombre_archivo = 'tasks.csv'
# fecha = '2024-07-14'
# hora = '15:30:00'
# descripcion = 'Nueva tarea con hora'

# agregar_tarea(nombre_archivo, fecha, hora, descripcion)



# x = """
# def filtrar_tareas():
#     def tareas_con_fecha(fecha):
#         df = pd.read_csv('tasks.csv')
#         df['Fecha'] = pd.to_datetime(df['Fecha'])
#         fecha = datetime.strptime(fecha, '%Y-%m-%d')
#         tareas_filtradas = df[df['Fecha'] == fecha]
#         return tareas_filtradas

#     fecha = '2024-07-18'
#     tareas_filtradas = tareas_con_fecha(fecha)
#     return tareas_filtradas
# filtrar_tareas()"""


# exec(x)

# # Llamar a la función y almacenar el resultado en t
# t = filtrar_tareas()

# # Imprimir el resultado
# print(t)


# x = """
# def filtrar_tareas(fecha):
#     df = pd.read_csv('tasks.csv')
#     df['Fecha'] = pd.to_datetime(df['Fecha'])
#     fecha = datetime.strptime(fecha, '%Y-%m-%d')
#     tareas_filtradas = df[df['Fecha'] == fecha]
#     return tareas_filtradas

# fecha = '2024-07-13'
# tareas_filtradas = filtrar_tareas(fecha)
# """
# exec(x)

# t = tareas_filtradas
# print(tareas_filtradas)
# today = datetime.today().strftime('%Y-%m-%d')
# print(f'HOY ES {today}')
df = pd.read_csv('tasks.csv')

df = df[df['Date'] != '2024-07-19']
df['Date'] =  pd.to_datetime(df['Date'])
x = df[df['Date'].dt.month == 9]
print(x)