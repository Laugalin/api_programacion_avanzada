# Este archivo nos ayudara a evitar las importaciones circulares
from flask_sqlalchemy import SQLAlchemy

# JWTManager es una clase que a través de atributos y de métodos
# Controla los procesos para generar JWTs y utilizarlos
from flask_jwt_extended import JWTManager

# Creeamos un  objeto de tipo SQLALchemy que va a controlar toda la base de datos
db =SQLAlchemy()

# Creeamos un objeto de una clase
jwt = JWTManager()

