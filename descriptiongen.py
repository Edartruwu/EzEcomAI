import json
import os
import replicate

def img_descriptiongen(image_path, prompt):
    output = replicate.run(
    "yorickvp/llava-13b:2facb4a474a0462c15041b78b1ad70952ea46b5ec6ad29583c0b29dbd4249591",
    input={
        "image": open(image_path, "rb"),
        "prompt": f"Eres un experto en la creación de descripciones de productos optimizadas para SEO para ventas en comercio electrónico. {prompt}",
        }
    )
    result = ""
    for item in output:
        result += item

    return result

image_folder = "images"  # Ruta de la carpeta de imágenes
output_data = {}  # Diccionario para almacenar los resultados

for filename in os.listdir(image_folder):
    if filename.endswith((".jpg", ".png")):
        image_path = os.path.join(image_folder, filename)
        description = img_descriptiongen(image_path, "Por favor, crea una descripción de producto convincente para este artículo.")
        output_data[filename] = description

# Guardar los resultados en un archivo JSON
with open("descriptions.json", "w") as json_file:
    json.dump(output_data, json_file, ensure_ascii=False, indent=4)
    