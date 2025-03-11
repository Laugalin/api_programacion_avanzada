#Flask es la libreria que nos ayuda a creear un servidor para nuestra API

from flask import Flask

#flask: Libreria
#Flask: modulo (clase)

#vamos a creear un objeto que contendra los metodos necesario para nuestro servidor 

app = Flask(__name__)



@app.route('/')
def pagina():
    return 'hola soy Laura :)'

app.run(port=8080)

#El metodo run le va a indicar a nuestro servidor que va a comenzar a recibir peticiones (servir)

#puerto 8080: le indica al usuario que accedera al  servidor que creeamos 
#púerto 22: Este puerto creea una conexion ssh con una computadora 
#puerto: 23 Telnet
#443: Este puerto usa https para enviar informacion 
#80: utiliza http para enviar informacion
#5432 SQL
#revisar cambios






