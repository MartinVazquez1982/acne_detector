import cv2
import numpy as np
import sys

src = None
mousedown = False
pts = []

def find_acne(img):
    '''
    Realiza el procesamiento de la imagen y la detección del acne
    
    Args:
        img (numpy.ndarray): Imagen de entrada para la deteccion del acne
        
    Returns:
        numpy.ndarray: Imagen con el acne detectado
    '''
    
    def color_check(color):
        '''
        Revisa que el color que fue enviado se encuentra en el rango de rojos del acne
        
        Args:
            color (tuple): Color a chequear
            
        Returns:
            boolean: Resultado de la corroboración del color
        '''
        return (0 <= color[0] <= 20) and (50 <= color[1] <= 255) and (50 <= color[2] <= 220)
    
    
    # PREPROCESAMIENTO
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 75)
    edges = cv2.dilate(edges, None, iterations=1)
    
    # SEGMENTACIÓN
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:

        # MEDICIÓN DE CARACTERISTICAS
        min_rect = cv2.boundingRect(contour)
        img_roi = img[min_rect[1]:min_rect[1]+min_rect[3], min_rect[0]:min_rect[0]+min_rect[2]]
        img_roi = cv2.cvtColor(img_roi, cv2.COLOR_BGR2HSV)
        color = cv2.mean(img_roi)
        img_roi = cv2.cvtColor(img_roi, cv2.COLOR_HSV2BGR)
        (center, radius) = cv2.minEnclosingCircle(contour)

        
        # CLASIFICACION
        if 3 < radius < 20 and color_check(color):
            cv2.rectangle(img, (min_rect[0], min_rect[1]), (min_rect[0]+min_rect[2], min_rect[1]+min_rect[3]), (0, 255, 0))        
    
    
    return img

def join_images(detection):
    '''
    Une el ane detecado con la imagen original
    
    Args:
        detection (numpy.ndarray): Imagen con la detección del acne
        
    Returns:
        numpy.ndarray: Union de la deteccion con la imagen original
    '''
    global src
    mask_blue = np.all(detection == [255, 0, 0], axis=-1)
    detection[mask_blue] = [255,255,255]
    mask = cv2.cvtColor(detection, cv2.COLOR_BGR2GRAY)
    mask[mask != 255] = 1
    result = src.copy()
    result[mask == 1] = detection[mask == 1]
    return result 
    

def on_mouse(event, x, y, flags, userdata):
    '''
    Maneja eventos del mouse en la ventana de visualización de OpenCV. Se realiza la selección 
    interactiva de una región de interés (ROI) en la imagen, que luego se utilizará para detectar el acné.
    Una vez marcada la zona, solicita la busqueda del acne y luego el postprocesamiento
    
    Args:
        event: Evento del mouse.
        x: Coordenada x del puntero del mouse.
        y: Coordenada y del puntero del mouse.
        flags: Proporcionan información adicional sobre el evento.
        userdata: Datos adicionales proporcionados al establecer el callback.
    '''
    global mousedown, pts

    if event == cv2.EVENT_LBUTTONDOWN:
        mousedown = True
        pts.clear()

    if event == cv2.EVENT_LBUTTONUP:
        mousedown = False
        if len(pts) > 2:
            mask = np.zeros(userdata.shape[:2], dtype=np.uint8)
            cv2.drawContours(mask, [np.array(pts)], 0, (255), -1)
            masked = np.full(userdata.shape, (255, 255, 255), dtype=np.uint8)
            cv2.bitwise_and(userdata, userdata, masked, mask=mask)
            masked = find_acne(masked)
            # POSTPROCESAMIENTO
            result = join_images(masked)
            cv2.imshow("Acne detector", result)

    if mousedown:
        if len(pts) > 2:
            cv2.line(userdata, (x, y), tuple(pts[-1]), (255, 0, 0))
        pts.append((x, y))
        cv2.imshow("Acne detector", userdata)

def acne_detection(path):
    '''
    Carga una imagen, crea una ventana interactiva para detectar acné facial y espera la interacción del usuario.
    
    Args:
        path (str): Path de la imagen a la que se le detectara el acne 
    '''
    global src
    src = cv2.imread(path)
    if src is None:
        return -1

    cv2.namedWindow("Acne detector", cv2.WINDOW_AUTOSIZE)
    cloneimg = src.copy()
    cv2.setMouseCallback("Acne detector", on_mouse, cloneimg)
    cv2.imshow("Acne detector", src)
    cv2.waitKey(0)
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python acne_detection.py <path_imagen>")
    else:
        path = sys.argv[1]
        acne_detection(path)