from models import Usuario
from extensions import jwt
from flask_jwt_extended import create_access_token


# La libreria DTETIME le permite a python trabajar con fechas y horas

#Time delta nos ayuda a hacer la conversion de dias, horas, minutos, etc. aun formato Linux
from datetime import timedelta

# Un archivo que contiene todas las acciones
# que un usuario puede realizar

# Nesesitamos un metodo para que el usuario pueda creear una cuenta
def crear_cuenta(nombre, correo, password):
    # Creeamos un objetio de tipo usuario que contendra la informacion para la db

    usuario_existente = Usuario.query.filter_by(email=correo).first()

    # Revisamos si lo que regresa esa query es diferente a None

    if usuario_existente is not None:
        print('El correo ya existe en la db')
        return{'status' : 'error', 'error' : 'La cuenta ya esta registrada'}
    
    # Esto solo se ejecuta si en la db no existe la cuenta que el ususrio esta registrando

    nuevo_usuario = Usuario(name=nombre, email=correo)

    nuevo_usuario.hashear_password(password_original=password)

    # Guardamos este nuevo objeto en la db
    nuevo_usuario.save()

    return{'status': 'ok', 'email':correo}

def iniciar_sesion(correo, password):

    # Que contenga usuarios filtrados a traveés de un parametro
    usuarios_existentes = Usuario.query.filter_by(email=correo).first()



    # 1.- Si el usuario existe. enntonces puede iniciar sesión
    

    # 2.- Si el usuario no existe en la db no puede iniciar sesión

    # Si el usuario no existe en la db no puede iniciar sesión
    if usuarios_existentes is None:
        print('La cuenta no existe')
        return {'status': 'error', 'error':'La cuenta no existe'}
    
    # Si la contraseña del formulario es de la db
    if usuarios_existentes.verificar_password(password_plano = password):
        
        # La variable indicara cuando caduca el token
        caducidad = timedelta(minutes=3)
    

        
        print('Inicio de sesión exitoso :D')
        token_de_acceso = create_access_token(identity=usuarios_existentes.name, expires_delta=caducidad)
        print(token_de_acceso)
        return {'status' : 'ok', 'token' : token_de_acceso}
    
    
        
    # Si el usuario existe pero la contraseña no coincide
    else:
        print('La contraseña es incorrecta')
        return {'status':'error','error':'Contraseña incorrecta :( '}

def encontrar_todos_los_usuarios():

    # Creamos una variable que contendra la respuesta de nuestra db
    usuarios = Usuario.query.all()

    print(usuarios)

    return usuarios
