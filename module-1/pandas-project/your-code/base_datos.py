import pandas as pd
import math
import re
import calendar
from datetime import datetime
import sys, traceback
import time

start_time = time.time()

print("\n==========================================================================================\n")
# Carga inicial del dataframe y eliminación de las columnas que hacen ruido
data_frame = pd.read_csv("attacks.csv", index_col=False, encoding="ISO-8859-1")
undesired_columns = [data_frame.columns[-2], data_frame.columns[-1]]
data_frame.drop(undesired_columns, axis=1, inplace=True)
data_frame.rename(columns={'Sex ': 'Sex', 'Species ': 'Species'}, inplace=True)
print("Procedimiento de carga, eliminación de columnas repetidas, renombrado de columnas finalizado")
print("\n==========================================================================================\n")

print("\n==========================================================================================\n")
print(f"El tamaño inicial de DF es{data_frame.shape}")
# Identificamos el número de columnas que deben ser null para eliminar el row
umbral_null = math.floor(len(data_frame.columns) * 0.65)
rows_a_eliminar = []
for index in data_frame.index:
    num_nulls = data_frame.iloc[index].isnull().sum()
    if num_nulls >= umbral_null:
        rows_a_eliminar.append(index)
print(f"Se han encontrado {len(rows_a_eliminar)} de filas con un 65% o mas de datos en null, son eliminadas")
data_frame.drop(rows_a_eliminar, axis=0, inplace=True)
print(f"Tamaño resultado del DF es{data_frame.shape}")
print("\n==========================================================================================\n")

print("\n==========================================================================================\n")
# Unificar columnas relacionadas a las fechas
rows_a_eliminar = []
for index in data_frame.index:
    try:
        nums = re.findall('\d', data_frame.iloc[index][0])
    except:
        nums = re.findall('\d', data_frame.iloc[index][18])

    if len(nums) >= 8:

        nums = nums[:8]
        anio = int("".join(nums[:4]))
        mes = int("".join(nums[4:6]))
        dia = int("".join(nums[6:]))

        # adecuamos las fechas al maximo y minimo mes y día en el mes
        if anio == 0:
            rows_a_eliminar.append(index)
            continue

        if not mes:
            mes = 1
        elif mes > 12:
            mes = 12

        if not dia:
            dia = 1
        elif dia > 31:
            dia = calendar.monthrange(anio, mes)[1]

        try:
            fecha = datetime(anio, mes, dia)
            data_frame._set_value(index=index, col='Date', value=pd.to_datetime(fecha, errors='coerce').date())
            # data_frame['Date'] = pd.to_datetime(fecha, errors='coerce')
        except:
            print(f"Encontre una excepción ---- {index}: error {anio},{mes},{dia}    num de caracteres {nums}")
            traceback.print_exc(file=sys.stdout)
    else:
        rows_a_eliminar.append(index)
print(f"Se han encontrado {len(rows_a_eliminar)} de filas sin fecha especifica, son eliminadas")
data_frame.drop(rows_a_eliminar, axis=0, inplace=True)
print(f"Se unifican las columnas Case Number[0], Date, Year, Case Number[19], Case Number[20] en la columna Date")
undesired_columns = [data_frame.columns[0], data_frame.columns[2], data_frame.columns[19], data_frame.columns[20]]
data_frame.drop(undesired_columns, axis=1, inplace=True)
print(f"Tamaño resultado del DF es{data_frame.shape}")
print("\n==========================================================================================\n")

print("\n==========================================================================================\n")
print("Proceso de estandarización de la columna 'Activity' en proceso")


# Procedo a remover los ing de la columna 'Activity' y estandarizar las entradas a capitalize
def estandarizar_actividad(input_val: str):
    input_val = str(input_val)
    if 'ing' not in input_val:
        input_val = "Not specified"
    output_val = input_val.capitalize()
    return output_val


data_frame['Activity'] = data_frame['Activity'].apply(lambda row: estandarizar_actividad(row))
print("Proceso de estandarización de la columna 'Activity' finalizado")
print("\n==========================================================================================\n")

print("\n==========================================================================================\n")
print("Proceso de estandarización de la columna 'Type' y limpieza en proceso")


# si la palabra contiene "boat" o "disaster" entonces transformarlo a unprovoked
# si la palabra es invalido entonces eliminarlo de la tabla porque no es un ataque de tiburon
# Todo lo demas se convierte en not especified
def estandarizar_tipo(input_val: str):
    input_val = str(input_val).lower()
    unprovoked_values = ['boat', 'disaster']
    accepted_values = ['unprovoked', 'provoked', 'invalid']
    input_val = str(input_val)

    for unprovoked_value in unprovoked_values:
        if unprovoked_value in input_val:
            input_val = 'unprovoked'

    if input_val not in accepted_values:
        input_val = "Not specified"

    output_val = input_val.capitalize()
    return output_val


data_frame['Type'] = data_frame['Type'].apply(lambda row: estandarizar_tipo(row))
print("Se han estandarizado los valores a 'Unprovoked', 'Provoked', 'Not specified' e 'Invalid'")
rows_a_eliminar = []
for index in data_frame.index:
    if data_frame.at[index, 'Type'] == 'Invalid':
        rows_a_eliminar.append(index)
data_frame.drop(rows_a_eliminar, axis=0, inplace=True)
print(f"Se remueven las filas que son invalidadas por el valor 'Invalid' en la columna 'Type')")
print(f"Tamaño resultado del DF es{data_frame.shape}")
print("\n==========================================================================================\n")

print("\n==========================================================================================\n")
print("Proceso de estandarización de la columna 'Name' y limpieza en proceso")


def estandarizar_nombres(input_val: str):
    input_val = str(input_val).lower()
    unnaccepted_vals = ["boat", "male", "female", "fisher", "child", "sailor", "ing", "man", "men", "boy", "girl",
                        "nan"]
    for unnaccepted_val in unnaccepted_vals:
        if unnaccepted_val in input_val:
            input_val = "not specified"
    return input_val.title()


data_frame['Name'] = data_frame['Name'].apply(lambda row: estandarizar_nombres(row))
print("Proceso de estandarización de la columna 'Name' y limpieza finalizado")
print("\n==========================================================================================\n")

print("\n==========================================================================================\n")
print("Proceso de estandarización de la columna 'Sex' en proceso")


def estandarizar_generos(input_val: str):
    input_val = str(input_val).upper()
    accepted_vals = ["F", "M"]
    for accepted_val in accepted_vals:
        if accepted_val in input_val:
            input_val = accepted_val
            return input_val.title()
    return "Not specified"


data_frame['Sex'] = data_frame['Sex'].apply(lambda row: estandarizar_generos(row))
print("Proceso de estandarización de la columna 'Sex' finalizado")
print("\n==========================================================================================\n")

print("\n==========================================================================================\n")
print("Proceso de estandarización de la columna 'Fatal (Y/N)' en proceso")


def estandarizar_fatal(input_val: str):
    input_val = str(input_val).upper()
    accepted_vals = ["Y", "N"]
    for accepted_val in accepted_vals:
        if accepted_val in input_val:
            input_val = accepted_val
            return input_val.title()
    return "Not specified"


data_frame['Fatal (Y/N)'] = data_frame['Fatal (Y/N)'].apply(lambda row: estandarizar_nombres(row))
print("Proceso de estandarización de la columna 'Fatal (Y/N)' finalizado")
print("\n==========================================================================================\n")

print("\n==========================================================================================\n")
print("Proceso de estandarización de la columna 'Age' en proceso")


def estandarizar_edad(input_val):
    input_val = str(input_val)

    edades = re.findall(r'\d*[0-9]', input_val)
    if len(edades) > 0:
        return "-".join(edades)
    else:
        return "Not specified"


data_frame['Age'] = data_frame['Age'].apply(lambda row: estandarizar_edad(row))
print("Proceso de estandarización de la columna 'Age' finalizado")
print("\n==========================================================================================\n")

print("\n==========================================================================================\n")
print("Proceso de estandarización de la columna 'Species' en proceso")


def estandarizar_especie(input_val):
    input_val = str(input_val).title()
    # ej: (?=\s+County) is a positive lookahead that asserts presence of 1 or more whitespaces followed by word County ahead of current match.
    tiburones = re.findall(r'\w+(?=\s+Shark)', input_val)

    for tiburon in tiburones:
        if len(tiburon) < 3:
            tiburones.remove(tiburon)

    if len(tiburones) > 0:
        return "-".join(tiburones)
    else:
        return "Not specified"


data_frame['Species'] = data_frame['Species'].apply(lambda row: estandarizar_especie(row))
print("Proceso de estandarización de la columna 'Species' finalizado")
print("\n==========================================================================================\n")

print("\n==========================================================================================\n")
print("Proceso de estandarización de la columna 'Time' en proceso")
for index in data_frame.index:
    temp_dato = str(data_frame.at[index, 'Time']).lower()
    if temp_dato == "nan" or len(temp_dato) < 2:
        data_frame._set_value(index=index, col='Time', value="Not specified")
        continue
    hora_minuto = re.findall(r'[^h]\d{1}', temp_dato)
    if len(hora_minuto) >= 2:
        data_frame._set_value(index=index, col='Time', value=":".join(hora_minuto[:2]))
print("Proceso de estandarización de la columna 'Time' finalizado")
print("\n==========================================================================================\n")

# Por emergencia elimino la columna duplicada de href formula
data_frame.drop("href formula", axis=1, inplace=True)
##Hago que la columna de Original order no tenga decimales ya que lo interpretaba con decimales
data_frame['original order'] = data_frame['original order'].apply(lambda row: int(row))
# Guardo el CSV, declaro el indice y cambio el encoding
data_frame.to_csv("attacks_cleaned.csv", index_label="Doc index", encoding="utf-8")
elapsed_time = time.time() - start_time
print(f"Finalizado en {elapsed_time} segundos")
