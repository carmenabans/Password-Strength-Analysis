import random

# Función para cargar palabras desde el archivo de diccionario
def load_dictionary(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file]
    return words

# Estrategia 1: Tomar 100 palabras aleatorias del diccionario
def generate_password_dic1(length, dictionary):
    return random.sample(dictionary, length)

# Estrategia 2: Cambiar entre mayúsculas y minúsculas
def generate_password_dic2(length, dictionary):
    passwords = random.sample(dictionary, length)
    for i in range(length):
        password = list(passwords[i])
        for j in range(len(password)):
            if password[j].islower():
                password[j] = password[j].upper()
            elif password[j].isupper():
                password[j] = password[j].lower()
        passwords[i] = ''.join(password)
    return passwords


# Estrategia 3: Reflejo
def generate_password_dic3(length, dictionary):
    passwords = random.sample(dictionary, length)  # Puedes quitar el random.sample si quieres procesar todas las palabras del diccionario
    result = []

    for word in passwords:
        reversed_word = word[::-1]  # Obtén el reflejo de la palabra
        doubled_word = word + reversed_word  # Duplícala
        result.append(doubled_word)

    return result



# Estrategia 4: Reemplazar letras con números y viceversa
def generate_password_dic4(length, dictionary):
    def replace_chars(char):
        replacements = {'o': '0', 'i': '1', 'e': '3', 'a': '4', 's': '5', 't': '7', 'b': '8'}
        return replacements.get(char, char)

    passwords = random.sample(dictionary, length)
    for i in range(length):
        passwords[i] = ''.join(replace_chars(char) for char in passwords[i])
    return passwords


# Estrategia 5: Revertir el orden de las letras
def generate_password_dic5(length, dictionary):
    passwords = random.sample(dictionary, length)
    for i in range(length):
        passwords[i] = passwords[i][::-1]
    return passwords

# Cargar el diccionario
dictionary = load_dictionary("rockyou-75.txt")

# Generar los cinco conjuntos de datos
dic1 = generate_password_dic1(100, dictionary)
dic2 = generate_password_dic2(100, dictionary)
dic3 = generate_password_dic3(100, dictionary)
dic4 = generate_password_dic4(100, dictionary)
dic5 = generate_password_dic5(100, dictionary)

print(dic1)
print()
print(dic2)
print()
print(dic3)
print()
print(dic4)
print()
print(dic5)

def write_to_txt(filename, data):
    with open(filename, 'w') as file:
        file.write('\n'.join(data))

# Leer el diccionario desde un archivo de texto en el mismo directorio
with open("rockyou-75.txt", "r") as file:
    dictionary = [line.strip() for line in file]


# Escribir la lista de palabras en un archivo de texto
write_to_txt("dic_1.txt", dic1)
write_to_txt("dic_2.txt", dic2)
write_to_txt("dic_3.txt", dic3)
write_to_txt("dic_4.txt", dic4)
write_to_txt("dic_5.txt", dic5)
