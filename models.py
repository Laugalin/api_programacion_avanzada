# SQL -> Querys
# El Traductor de python a sql es la herramienta SQLAlchemy
from extensions import db

# Vamos a importar el modulo para hashear las contraseñas
from werkzeug.security import check_password_hash, generate_password_hash

# generate_password_hash recibe un texto en una serie de caracteres
# Con longitud igual en todos los casos

# Check_password_hash recibe dos datos:
# 1.- El hash que esta en la base de datos 
# 2.- La contraseña que el usuario escribió



# Vamos a crear un modelo 
# Un modelo es un plano de como se ve la tabla en sql
class Usuario(db.Model):
  __tablename__ = 'usuarios'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  email = db.Column(db.String(80), nullable=False)
  password = db.Column(db.String, nullable=False)



  # Tenemos el metodo para cifrar las contraseñas
  def hashear_password(self, password_original):
    self.password = generate_password_hash (password_original)


  def verificar_password(self,passwor_plano):
    return check_password_hash(self.password,passwor_plano)


  def save(self):
    # Creamos una conexion con la base de datos para añadir información
    db.session.add(self)

    # Nos aseguramos de que los cambios se hagan
    db.session.commit()

  
  def delete(self):
    db.session.delete(self)

    # Nos aseguramos de que los cambios se guarden
    db.session.commit()

