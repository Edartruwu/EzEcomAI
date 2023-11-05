import json
import csv

# Define una función para eliminar las extensiones .jpg y .png de una cadena de texto
def remove_image_extensions(text):
    return text.replace('.jpg', '').replace('.png', '')

# Lee el archivo JSON
with open('descriptions.json', 'r') as json_file:
    data = json.load(json_file)

# Crear un archivo CSV para escribir los resultados
with open('resultado.csv', 'w', newline='') as csv_file:
    fieldnames = ['name', 'description']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for nombre, descripcion in data.items():
        # Elimina las extensiones .jpg y .png de nombre y descripcion
        clean_nombre = remove_image_extensions(nombre)
        clean_descripcion = remove_image_extensions(descripcion)

        # Escribe la entrada limpia en el archivo CSV
        writer.writerow({'name': clean_nombre, 'description': clean_descripcion})

# Notifica al usuario que el proceso ha finalizado
print("El archivo resultado.csv ha sido creado correctamente.")
