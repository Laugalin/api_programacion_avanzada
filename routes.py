#Este archivo va a almacenar unica y exclusivamente rutas de nuestro servidor 

from flask import Flask, render_template, request, redirect, url_for, make_response

from methods import crear_cuenta, iniciar_sesion, encontrar_usuario_por_id

from flask_jwt_extended import decode_token, verify_jwt_in_request, get_jwt_identity



firma = '0Bjk5fTiU6VtsbLILf9HFX6UMc2R5b'

def cargar_rutas(app):

#Este bloque de codigo es la base para todas las rutas 
    @app.route('/')
    def index():
        # Buscamos todos los dato de la tabla "usuarios"

        logged = False
        try:
            
        # La aplicación va a revisar si existe la cookie de acceso
            verify_jwt_in_request()
            logged = True
  
        except Exception as error:
            logged = False
            print(error)





        return render_template('index.html', logged=logged)


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


    @app.route('/usuario')
    def pantalla_usuario():
        try:
            # La aplicación va a revisar si existe la cookie de acceso
            verify_jwt_in_request()

            nombre_de_usuario = get_jwt_identity()

            id_del_usuario = request.args.get('user_id')

            datos_usuario = encontrar_usuario_por_id(id_del_usuario)

            datos_usuario =[datos_usuario.id, datos_usuario.name, datos_usuario.email]

            print(datos_usuario)

            #print(f'El ID que viene en los argumentos es : {id_del_usuario}')


            return render_template('user.html', user_data=datos_usuario)

        except Exception as error:
            print('La cookie no existe o esta mal')
            print(f'La razón es : {error}')

            return redirect(url_for('login'))

    @app.route('/logout')
    def cerrar_sesion():
        respuesta = make_response(redirect(url_for('index')))
        respuesta.set_cookie('access_token', '')

        return respuesta
    
    @app.route('/user_info')
    def obtener_info_usuario():
        try:
            verify_jwt_in_request()
            # Obtenemos el token del usuario a traves de la cookie
            user_token = request.cookies.get('access_token')

            token_info = decode_token(user_token)

            id_usuario = token_info['user_id']
            print(id_usuario)

            return redirect(url_for('pantalla_usuario', user_id=id_usuario))

        except Exception as error:
            print(error)
            return redirect(url_for('index'))

        #datos_usuario = encontrar_usuario_por_id()

        

    



                                                                       