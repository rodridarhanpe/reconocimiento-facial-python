import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

#crear base de datos
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados  = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

#codificar imagenes
def codificar(imagenes):

    #crar lista nueva
    lista_codificada = []

    #pasar todas las imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        #codificar
        codificado = fr.face_encodings(imagen)[0]

        #agregar a la lista
        lista_codificada.append(codificado)

    #devolver lista codificada
    return lista_codificada

#REGISTRAR INGRESOS
def registrar_ingresos(persona):
    with open('registro.csv', 'a+') as f:
        f.seek(0)
        lista_datos = f.readlines()
        nombres_registro = []

        for linea in lista_datos:
            ingreso = linea.split(',')
            nombres_registro.append(ingreso[0])

        if persona not in nombres_registro:
            ahora = datetime.now()
            string_ahora = ahora.strftime('%H:%M:%S')
            f.write(f'{persona},{string_ahora}\n')

lista_empleados_codificada = codificar(mis_imagenes)

#tomar una imagen de camara web
captura = cv2.VideoCapture(0)

registrado = False

#leer imagene de la camara
while True:
    exito, imagen = captura.read()

    if not exito:
        print("No se ha podido tomar la captura")
        break

    cara_captura = fr.face_locations(imagen)
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)
        indice_coincidencia = numpy.argmin(distancias)

        if distancias[indice_coincidencia] < 0.6 and not registrado:
            nombre = nombres_empleados[indice_coincidencia]

            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))

            registrar_ingresos(nombre)
            print(f"Ingreso registrado: {nombre}")

            registrado = True
            break

    if registrado:
        break

    cv2.imshow('Imagen web', imagen)

    if cv2.waitKey(1) & 0xFF == 27:
        break

captura.release()
cv2.destroyAllWindows()