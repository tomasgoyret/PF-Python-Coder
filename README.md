# PF-Python-Coder
## Entrega intermedia del proyecto final


#### __Aspectos principales para tener en cuenta__: 

En el archivo settings.py que se encuentra en la carpeta Entregable1 se debe tener configurada la ruta para los template correspondiente en tu ordenador(linea 58 )

En VSC hacer click derecho en la carpeta template que se encuentra en EntregableApp, luego hacer click en copy path y pegar en la linea 58 del archivo settings.py en la carpeta Entregable 1 de la misma manera que se encuentra (teniendo en cuenta el formato)

#### __Pruebas__

Para empezar, encender la app con el comando python manage.py runserver y luego situarse en el navegador en la url __http://127.0.0.1:8000/EntregableApp/inicio__ . Esta es la página de inicio

#### _Navegacion General_ : 


La navegacion cuenta de 7 secciones: 

    -Familia Segunda : donde unicamente se renderizan los familiares segundos
    -Bienes : donde unicamente se renderizan los bienes familiares
    -Familia : donde unicamente se renderizan los familiares directos
    -Formulario Familia:  donde se agregan familiares directos.
    -Formulario Bienes:  donde se agregan bienes familiares.
    -Formulario Familia Segunda:  donde se agregan familiares segundos.
    -Busqueda: Donde buscamos busqueda de familia directa.

Prueba de formularios: 

    Completar los formularios con la información que se indica.
    __IMPORTANTE__ : Completar la fecha de nacimiento con el formato YYYY-MM-DD para los casos de familia directa y segunda

    Luego de tocar enviar podemos ir a la seccion donde renderizan y comprobar que se agregaron correctamente.


Prueba de búsqueda:
    
    Ingresar el nombre del familiar que se desea buscar