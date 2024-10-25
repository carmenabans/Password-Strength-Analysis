import re
import statistics

# Variables para almacenar los datos
cracked_passwords = 0
times = []

# Abre el archivo de log
with open("john.log", "r") as log_file:
    for line in log_file:
        # Busca líneas que indiquen que una contraseña fue descifrada
        if "Cracked" in line:
            cracked_passwords += 1
        # Busca líneas que contengan el tiempo requerido (formato: 0:00:00:01)
        elif re.search(r'\d:\d{2}:\d{2}:\d{2}', line):
            time_parts = line.split()
            for part in time_parts:
                if re.match(r'\d:\d{2}:\d{2}:\d{2}', part):
                    time_str = part
                    # Convierte el tiempo a segundos (se asume que el tiempo es de formato hh:mm:ss:dd)
                    h, m, s, d = map(int, time_str.split(':'))
                    total_seconds = h * 3600 + m * 60 + s + d / 100
                    times.append(total_seconds)

# Calcula el porcentaje de contraseñas rotas
total_hashes = 100  # Ajusta esto al número total de contraseñas en tus datos
percentage_cracked = (cracked_passwords / total_hashes) * 100

# Calcula la media y la mediana del tiempo requerido
mean_time = statistics.mean(times)
median_time = statistics.median(times)

# Imprime los resultados
print(f"Porcentaje de contraseñas rotas: {percentage_cracked:.2f}%")
print(f"Media del tiempo requerido (en segundos): {mean_time:.2f}")
print(f"Mediana del tiempo requerido (en segundos): {median_time:.2f}")

