Reconocimiento Facial con Python

Proyecto de reconocimiento facial en tiempo real utilizando Python,
OpenCV y la librería `face_recognition`. El sistema detecta rostros a
través de la cámara web, los compara con una base de imágenes conocidas
y registra los ingresos en un archivo CSV.

Para facilitar las pruebas, la base de datos utiliza imágenes de personas públicas.

Funcionalidades

-   Captura de video en tiempo real desde la webcam
-   Detección y reconocimiento de rostros
-   Comparación con una base de imágenes conocidas
-   Registro automático de ingresos con horario
-   Visualización del rostro detectado y su nombre

Tecnologías utilizadas

-   Python 3
-   OpenCV
-   face_recognition (dlib)
-   NumPy

Estructura del proyecto

reconocimiento-facial-python/ │ ├── reconocimiento/ │ ├── facial.py │
└── Empleados/ │ ├── Messi.jpeg │ ├── Ronaldo.jpeg │ ├── Neymar.jpg │
└── ... │ ├── requirements.txt ├── .gitignore └── README.md

Instalación y ejecución

Clonar el repositorio

git clone
https://github.com/rodridarhanpe/reconocimiento-facial-python.git cd
reconocimiento-facial-python

Crear y activar entorno virtual

python3 -m venv .venv source .venv/bin/activate

Instalar dependencias

pip install -r requirements.txt

Ejecutar el programa

python reconocimiento/facial.py

Registro de ingresos

Los reconocimientos exitosos se guardan automáticamente en un archivo
`registro.csv` con el nombre de la persona y la hora del ingreso.

Notas

-   Es necesario contar con una cámara web funcional.
-   Las imágenes dentro de la carpeta `Empleados` deben contener un solo
    rostro por imagen.
-   El proyecto está pensado con fines educativos y de práctica.


Autor

Rodrigo Darhanpé\
Proyecto realizado como práctica de Python y visión por computadora.
