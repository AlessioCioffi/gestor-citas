Instalación:

Clona este repositorio en tu máquina local utilizando Git:
bash

git clone https://github.com/AlessioCioffi/gestor-citas.git

Ve al directorio del proyecto
Crea un entorno virtual para el proyecto:

python -m venv venv

Activa el entorno virtual:
En Windows:

venv\Scripts\activate

En macOS y Linux:

source venv/bin/activate

Instala las dependencias del proyecto desde el archivo requirements.txt:
pip install -r requirements.txt

Para ejecutar el servidor de desarrollo de Django, usa el siguiente comando:
python manage.py runserver

Ahora, abre tu navegador y accede a http://127.0.0.1:8000/ para ver la página principal del gestor de citas.
