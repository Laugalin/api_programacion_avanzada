#contraseña: fDYn6No75wFd
#Flask es la libreria que nos ayuda a creear un servidor para nuestra API

from flask import Flask


# Desde el archivo routes quiero que importe la funcion "Cargar_rutas"
from routes import cargar_rutas

from extensions import db

#flask: Libreria
#Flask: modulo (clase)

#vamos a creear un objeto que contendra los metodos necesario para nuestro servidor 

app = Flask(__name__)

# 1.- Configuramos la app para conectarse a una db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.ibgojbihyyldlfgoudxa:fDYn6No75wFd@aws-0-us-east-1.pooler.supabase.com:6543/postgres'

# 2.- Desactivamos el seguimiento de modificaciones

app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Cargamos las rutas creadas desde el archivo routes.py


cargar_rutas(app)

app.run(port=8080, debug=True)                                                       

#El metodo run le va a indicar a nuestro servidor que va a comenzar a recibir peticiones (servir)

#puerto 8080: le indica al usuario que accedera al  servidor que creeamos 
#púerto 22: Este puerto creea una conexion ssh con una computadora 
#puerto: 23 Telnet
#443: Este puerto usa https para enviar informacion 
#80: utiliza http para enviar informacion
#5432 SQL
#revisar cambios






