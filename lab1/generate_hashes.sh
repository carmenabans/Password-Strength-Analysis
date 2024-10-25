#!/bin/bash

# Comprueba si no se proporcionaron archivos de entrada
if [ $# -eq 0 ]; then
    echo "Debes proporcionar al menos un archivo como entrada."
    exit 1
fi

for input_file in "$@"; do
    # Comprueba si el archivo de entrada existe
    if [ ! -f "$input_file" ]; then
        echo "El archivo $input_file no existe. Continuando con el siguiente archivo."
        continue
    fi

    # Nombre del archivo de salida (incluye el nombre original más "_hash.txt")
    output_file="${input_file%.*}_hash_md5.txt"

    # Inicializa el archivo de hashes o lo sobrescribe si ya existe
    > "$output_file"

    # Procesa cada línea del archivo de entrada y genera el hash con MD5Crypt
    while IFS= read -r password; do
        hash=$(mkpasswd --method=md5crypt "$password")
        echo "$hash" >> "$output_file"
    done < "$input_file"

    echo "Los hashes se han generado en $output_file."
done

