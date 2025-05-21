# Este archivo nos ayudara a evitar las importaciones circulares
from flask_sqlalchemy import SQLAlchemy

# Creeamos un  objeto de tipo SQLALchemy que va a controlar toda la base de datos
db =SQLAlchemy()