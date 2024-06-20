import cv2
import os

def draw_bounding_box(image_path, label_path):
    # Leer la imagen
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Leer el archivo de etiquetas
    with open(label_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Parsear la línea
        class_id, x_center, y_center, box_width, box_height = map(float, line.split())

        # Convertir coordenadas normalizadas a coordenadas en píxeles
        x_center *= width
        y_center *= height
        box_width *= width
        box_height *= height

        # Calcular las coordenadas del bounding box
        x_min = int(x_center - (box_width / 2))
        y_min = int(y_center - (box_height / 2))
        x_max = int(x_center + (box_width / 2))
        y_max = int(y_center + (box_height / 2))

        # Dibujar el bounding box en la imagen
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
    
    cv2.imshow("Acne detector", image)
    cv2.waitKey(0)

def obtener_nombre_sin_extension(ruta_archivo):
    nombre_archivo = os.path.basename(ruta_archivo)  # Obtiene el nombre del archivo con la extensión
    nombre_sin_extension = os.path.splitext(nombre_archivo)[0]  # Elimina la extensión
    return nombre_sin_extension

for file_name in os.listdir(r'C:\\Users\\s7tan\\OneDrive\\Desktop\\Universidad\\Procesamiento de Imagenes\\Project\\Data\\Acne detection.v1i.yolov8\\valid\\images'):
    label_path = os.path.join(r'C:\\Users\\s7tan\\OneDrive\\Desktop\\Universidad\\Procesamiento de Imagenes\\Project\\Data\\Acne detection.v1i.yolov8\\valid', 'labels', obtener_nombre_sin_extension(file_name)+'.txt')
    file_name = os.path.join(r'C:\\Users\\s7tan\\OneDrive\\Desktop\\Universidad\\Procesamiento de Imagenes\\Project\\Data\\Acne detection.v1i.yolov8\\valid\\images', file_name)
    draw_bounding_box(file_name, label_path)
