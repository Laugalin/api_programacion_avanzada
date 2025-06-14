#Este archivo va a almacenar unica y exclusivamente rutas de nuestro servidor 

from flask import Flask, render_template, request, redirect, url_for, make_response

from methods import crear_cuenta, iniciar_sesion, encontrar_todos_los_usuarios

def cargar_rutas(app):

#Este bloque de codigo es la base para todas las rutas 
    @app.route('/')
    def index():
        # Buscamos todos los dato de la tabla "usuarios"


        return render_template('index.html')


    #Esta es otra ruta
    @app.route('/login')
    def login():

        resultado = request.args.get('status')

        return render_template('login.html', estado=resultado)

    #Esta es otra ruta
    @app.route('/signup')
    def signup():

        resultado = request.args.get('status')


        return render_template('signup.html', estado=resultado)


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
        
        respuesta_login = iniciar_sesion(email, password)



        if respuesta_login['status'] == 'error':
            return redirect(url_for('login', status=respuesta_login['status']))
        
        # Si lo de arriba no se cumple, significa que tenemos un token
        respuesta = make_response(redirect(url_for('index')))

        respuesta.set_cookie('access_token',respuesta_login['token'], secure=True, max_age=3600)

        
        return respuesta

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
        
        respuesta_signup = crear_cuenta(nombre, email, password)

        print(respuesta_signup)

        if respuesta_signup['status'] == 'error':
            return redirect(url_for('signup', status=respuesta_signup['status']))

        
        return redirect(url_for('index', status=respuesta_signup ['status']))

    



    
    @app.route('/error')
    def pantalla_error():
        return render_template('error.html')




                                                                       