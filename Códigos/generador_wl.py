import random
import string

# WORDLIST 1 - PARA LETRAS MINUS Y MAYUS
def generate_wl_1(length):
    characters = string.ascii_letters
    return [''.join(random.choice(characters) for _ in range(length)) for _ in range(60000)]

# WORDLIST 2 - PARA ANS Y NUMEROS
def generate_password_num(length):
    characters = string.digits
    return [''.join(random.choice(characters) for _ in range(length)) for _ in range(20000)]

def generate_password_ans(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return [''.join(random.choice(characters) for _ in range(length)) for _ in range(40000)]

# Función para escribir los datos en un archivo
def write_to_txt(filename, data):
    with open(filename, 'w') as file:
        file.write('\n'.join(data))

dic1 = generate_wl_1(7)  # Cambia la longitud según tus necesidades
dic2 = generate_password_num(7)  # Cambia la longitud según tus necesidades
dic2 += generate_password_ans(7)  # Cambia la longitud según tus necesidades

write_to_txt("wordlist_1.txt", dic1)
write_to_txt("wordlist_2.txt", dic2)

