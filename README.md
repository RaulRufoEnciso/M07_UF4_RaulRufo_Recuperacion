PARTE DE MODELOS - PRACTICA 17

Primero creamos la base de datos y la dejamos vacia
![img_4.png](img_4.png)

Ahora vamos al proyecto y creamos los modelos de Alumnos,  
![img_1.png](img_1.png)

y de Profesores  
![img_2.png](img_2.png)

Despues hacemos la migracion con makemigration y migracion
![img.png](img.png)

Y por ultimo vamos a la base de datos y 
comprovamos que estan creadas las migraciones

![img_3.png](img_3.png)

PARTE DE FORMULARIOS - PRACTICA 18

Primero creamos el archivo form.py en el que haremos la 
consulta al modelo para extraer los campos de la tabla.      
![img_5.png](img_5.png)

Despues nos dirijiremos a las views y crearemos los metodos
para contactar con la tabla y hacer el POST para enviar los
datos recogidos del formulario y enviarlos a la base de datos.   
![img_6.png](img_6.png)       
![img_10.png](img_10.png)     

Para acabar crearemos en la carpeta templates una subcarpeta 
llamada formularios en los que añadiremos los dos form.html.
![img_7.png](img_7.png)      
![img_8.png](img_8.png)     

Finalmente le asignaremos las rutas en el archivo urls.py de 
nuestra app a los metodos y ajustaremos el index.html para 
poder mostar los formularios.  
![img_9.png](img_9.png)         
![img_11.png](img_11.png)
