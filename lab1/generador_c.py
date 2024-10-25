import os
import random
import string

# Directorio actual
directorio_actual = os.getcwd()

# Número de archivos a crear
num_archivos = 5

# Número de contraseñas por archivo
num_contrasenas = 100

# Longitud de las contraseñas
longitud_contrasena = 3

# Funciones para generar contraseñas
def generate_password_minus(length):
    characters = string.ascii_lowercase
    return ''.join(random.choice(characters) for _ in range(length))

def generate_password_mayus(length):
    characters = string.ascii_uppercase
    return ''.join(random.choice(characters) for _ in range(length))

def generate_password_num(length):
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_password_ans(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Bucle para crear los archivos y agregar contraseñas minus
longitud_contrasena = 3
for i in range(num_archivos):
    nombre_archivo = f"minus_{longitud_contrasena}.txt"
    with open(nombre_archivo, 'w') as archivo:
        for j in range(num_contrasenas):
            contrasena = generate_password_minus(longitud_contrasena)
            archivo.write(contrasena + '\n')
    longitud_contrasena += 1

print(f"Se han creado {num_archivos} archivos de contraseñas minus en el directorio actual: {directorio_actual}")

# Bucle para crear los archivos y agregar contraseñas mayus
longitud_contrasena = 3
for i in range(num_archivos):
    nombre_archivo = f"mayus_{longitud_contrasena}.txt"
    with open(nombre_archivo, 'w') as archivo:
        for j in range(num_contrasenas):
            contrasena = generate_password_mayus(longitud_contrasena)
            archivo.write(contrasena + '\n')
    longitud_contrasena += 1

print(f"Se han creado {num_archivos} archivos de contraseñas mayus en el directorio actual: {directorio_actual}")

# Bucle para crear los archivos y agregar contraseñas num
longitud_contrasena = 3
for i in range(num_archivos):
    nombre_archivo = f"num_{longitud_contrasena}.txt"
    with open(nombre_archivo, 'w') as archivo:
        for j in range(num_contrasenas):
            contrasena = generate_password_num(longitud_contrasena)
            archivo.write(contrasena + '\n')
    longitud_contrasena += 1

print(f"Se han creado {num_archivos} archivos de contrasenas num en el directorio actual: {directorio_actual}")

# Bucle para crear los archivos y agregar contraseñas ans
longitud_contrasena = 3
for i in range(num_archivos):
    nombre_archivo = f"ans_{longitud_contrasena}.txt"
    with open(nombre_archivo, 'w') as archivo:
        for j in range(num_contrasenas):
            contrasena = generate_password_ans(longitud_contrasena)
            archivo.write(contrasena + '\n')
    longitud_contrasena += 1

print(f"Se han creado {num_archivos} archivos de contrasenas ans en el directorio actual: {directorio_actual}")

