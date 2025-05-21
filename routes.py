#Este archivo va a almacenar unica y exclusivamente rutas de nuestro servidor 

from flask import Flask, render_template, request, redirect, url_for

from methods import crear_cuenta, iniciar_sesion, encontrar_todos_los_usuarios

def cargar_rutas(app):

#Este bloque de codigo es la base para todas las rutas 
    @app.route('/')
    def index():
        # Buscamos todos los dato de la tabla "usuarios"

        lista_usuarios = encontrar_todos_los_usuarios()

        for usuario in lista_usuarios:
            print(f'''
        nombre usuario: {usuario.name}
        correo usuario: {usuario.email}
        contraseña usuario: {usuario.password}

''')
        return render_template('index.html')


    #Esta es otra ruta
    @app.route('/login')
    def login():
        return render_template('login.html')

    #Esta es otra ruta
    @app.route('/signup')
    def signup():
        return render_template('signup.html')


    #Esta ruta va a manejar la informacion
    #Este metodo solo funcionara para el inicio de sesion 

    @app.route('/manipulacion', methods=['POST'])
    def manipular_datos():
        email = request.form.get('email')
        password = request.form.get('password')
        
        print(f'''
            email : {email}
            contraseña: {password}
    ''')
        
        iniciar_sesion()
        
        return redirect(url_for('index'))

    #intersectamos la informacion del Sign Up del usuario
    @app.route('/datos_crear_cuenta', methods=['post'])
    def obtener_datos_cuenta():
        nombre = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        print(f'''
        nombre: {nombre}
        correo: {email}
        password: {password}
    ''')
        
        crear_cuenta(nombre, email, password)
        
        return redirect(url_for('index'))


                                                                       