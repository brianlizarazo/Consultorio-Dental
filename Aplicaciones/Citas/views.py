from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime, date
from babel.dates import format_date, format_time
from .enviar_email import enviar_email, enviar_mensaje
from .models import *
from .validaciones import *

# Create your views here.

# Vista que renderiza la página principal del sitio web de la Clínica Dental Díaz
def index(request):
    return render(request, 'index.html')

# ===========================
#          SERVICIOS
# ===========================

# Vista que renderiza la página de odontología general
def odontologiaGeneral(request):
    return render(request, 'servicios/odontologia-general.html')

# Vista que renderiza la página de limpieza dental
def limpiezaDental(request):
    return render(request, 'servicios/limpieza-dental.html')

# Vista que renderiza la página de periodoncia
def periodoncia(request):
    return render(request, 'servicios/periodoncia.html')

# Vista que renderiza la página de prótesis removibles
def protesisRemovibles(request):
    return render(request, 'servicios/protesis-removibles.html')

# Vista que renderiza la página de tratamiento de caries
def tratamientoDeCaries(request):
    return render(request, 'servicios/tratamiento-de-caries.html')

# Vista que renderiza la página de tratamiento de conducto
def tratamientoDeConducto(request):
    return render(request, 'servicios/tratamiento-de-conducto.html')

# Vista que renderiza la página de evaluación clínica y radiográfica
def evaluacionRadiografica(request):
    return render(request, 'servicios/evaluacion-radiografica.html')

# Vista que renderiza la página de coronas y puentes
def coronasYPuentes(request):
    return render(request, 'servicios/coronas-y-puentes.html')

# ==========================================
#               SOBRE NOSOTROS
# ==========================================

# Vista que renderiza la página de 'Sobre nosotros' del sitio web de la Clínica Dental Díaz
def sobreNosotros(request):
    return render(request, 'secciones/sobre-nosotros.html')

# ===========================
#          CONTACTOS
# ===========================

# Vista que renderiza la página de contacto del sitio web de la Clínica Dental Díaz
def contactos(request):
    return render(request, 'secciones/contactos.html')

# Vista que procesa el envío de un comentario por correo electrónico desde la página 'Contáctanos'
def procesarMensaje(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        phone = request.POST['phone']
        mensaje = request.POST['mensaje']

        if campo_vacio(nombre):
            return JsonResponse(objeto_error('nombre', 'Campo vacío', 'Debe completar el campo con el nombre', 'error', 'Completar'))

        if solo_espacios_en_blanco(nombre):
            return JsonResponse(objeto_error('nombre', 'Espacios en blanco', 'El nombre no puede estar compuesto sólo de espacios en blanco', 'error', 'Corregir'))

        if not comprobar_escritura(nombre):
            return JsonResponse(objeto_error('nombre', 'Nombre inválido', 'El nombre ingresado no cumple con el estándar definido', 'error', 'Corregir'))

        if campo_vacio(apellido):
            return JsonResponse(objeto_error('apellido', 'Campo vacío', 'Debe completar el campo con el apellido', 'error', 'Completar'))

        if solo_espacios_en_blanco(apellido):
            return JsonResponse(objeto_error('apellido', 'Espacios en blanco', 'El apellido no puede estar compuesto sólo de espacios en blanco', 'error', 'Corregir'))

        if not comprobar_escritura(apellido):
            return JsonResponse(objeto_error('apellido', 'Apellido inválido', 'El apellido ingresado no cumple con el estándar definido', 'error', 'Corregir'))

        if campo_vacio(email):
            return JsonResponse(objeto_error('email', 'Campo vacío', 'Debe completar el campo con el correo electrónico', 'error', 'Completar'))
        elif not email_correcto(email):
            return JsonResponse(objeto_error('email', 'Correo electrónico inválido', 'El correo electrónico ingresado no cumple con el formato especificado', 'error', 'Corregir'))
        elif not Dominio.objects.filter(descripcion_dominio = email[email.find("@"):]):
            return JsonResponse(objeto_error('email', 'Dominio web inválido', 'No se reconoce el nombre de dominio del correo electrónico ingresado', 'warning', 'Corregir'))
        
        if campo_vacio(phone):
            return JsonResponse(objeto_error('phone', 'Campo vacío', 'Debe completar el campo con el número de teléfono', 'error', 'Completar'))
        if not phone_correcto(phone):
            return JsonResponse(objeto_error('phone', 'Teléfono inválido', 'El número de teléfono ingresado no cumple con el formato especificado', 'error', 'Corregir'))
        elif not Area.objects.filter(cod_area = phone[:4]):
            return JsonResponse(objeto_error('phone', 'Código de área inválido', 'No se reconoce el código de área del número de teléfono ingresado', 'warning', 'Corregir'))
        
        enviar_mensaje(nombre, apellido, email, phone, mensaje)

        return JsonResponse(objeto_success('¡Envío exitoso!', '¡Su mensaje ha sido enviado con éxito!', 'success', 'Aceptar'))

# ================================================
#                 INICIO DE SESIÓN
# ================================================

# Vista que renderiza la página de inicio de sesión del sitio web de la Clínica Dental Díaz
def login(request):
    return render(request, 'secciones/login.html')

# Vista que procesa el registro de un usuario
def registrarUsuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password_entered = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']

        if campo_vacio(username):
            return JsonResponse(objeto_error('username', 'Campo vacío', 'Debe completar el campo con el nombre de usuario', 'error', 'Completar'))

        if not longitud_username_correcta(username):
            return JsonResponse(objeto_error('username', 'Longitud incorrecta', 'El nombre de usuario debe tener entre 6 y 30 caracteres', 'error', 'Cambiar'))

        if tiene_espacios_en_blanco(username):
            return JsonResponse(objeto_error('username', 'Espacios en blanco', 'El nombre de usuario no puede contener espacios en blanco', 'error', 'Cambiar'))
            
        if tiene_caracteres_especiales(username):
            return JsonResponse(objeto_error('username', 'Caracteres especiales', "El nombre de usuario no puede contener caracteres especiales, aparte del punto '.'", 'error', 'Cambiar'))

        if inicia_termina_con_punto(username):
            return JsonResponse(objeto_error('username', 'Inicia o termina en punto', "El nombre de usuario no puede iniciar o terminar con un punto '.'", 'warning', 'Cambiar'))

        if dos_puntos_consecutivos(username):
            return JsonResponse(objeto_error('username', 'Dos puntos consecutivos', "El nombre de usuario no puede contener dos puntos '..' consecutivos", 'warning', 'Cambiar'))

        if Usuario.objects.filter(username = username):
            return JsonResponse(objeto_error('username', 'Nombre de usuario ocupado', 'El nombre de usuario ingresado ya se encuentra en uso. Intente nuevamente', 'warning', 'Cambiar'))
        
        if campo_vacio(password_entered):
            return JsonResponse(objeto_error('password', 'Campo vacío', 'Debe completar el campo con la contraseña', 'error', 'Completar'))

        if not longitud_password_correcta(password_entered):
            return JsonResponse(objeto_error('password', 'Longitud incorrecta', 'La contraseña debe tener entre 14 y 127 caracteres', 'error', 'Cambiar'))

        if not password_segura(password_entered):
            return JsonResponse(objeto_error('password', 'Contraseña débil', 'La contraseña debe contener mayúsculas, minúsculas, números y al menos un caracter especial', 'error', 'Cambiar'))
        
        if campo_vacio(email):
            return JsonResponse(objeto_error('email', 'Campo vacío', 'Debe completar el campo con el correo electrónico', 'error', 'Completar'))

        if not email_correcto(email):
            return JsonResponse(objeto_error('email', 'Correo electrónico inválido', 'El correo electrónico ingresado no cumple con el formato especificado', 'error', 'Cambiar'))
         
        if not Dominio.objects.filter(descripcion_dominio = email[email.find("@"):]):
            return JsonResponse(objeto_error('email', 'Dominio web inválido', 'No se reconoce el nombre de dominio del correo electrónico', 'warning', 'Cambiar'))

        if Usuario.objects.filter(email = email.lower()):
            return JsonResponse(objeto_error('email', 'Correo electrónico ocupado', 'El correo electrónico ingresado ya se encuentra en uso', 'warning', 'Cambiar'))
        
        if campo_vacio(phone):
            return JsonResponse(objeto_error('phone', 'Campo vacío', 'Debe completar el campo con el número de teléfono', 'error', 'Completar'))

        if not phone_correcto(phone):
            return JsonResponse(objeto_error('phone', 'Número de teléfono inválido', 'El número de teléfono ingresado no cumple con el formato especificado', 'error', 'Cambiar'))
        
        if not Area.objects.filter(cod_area = phone[:4]):
            return JsonResponse(objeto_error('phone', 'Código de área inválido', 'No se reconoce el código de área del número de teléfono', 'warning', 'Cambiar'))
        
        if Usuario.objects.filter(phone_number = phone):
            return JsonResponse(objeto_error('phone', 'Número de teléfono ocupado', 'El número de teléfono ingresado ya se encuentra en uso', 'warning', 'Cambiar'))
        
        hashed_salted_password = make_password(password_entered)
        print(hashed_salted_password)

        Usuario.objects.create(username = username.lower(), hashed_salted_password = hashed_salted_password, email = email.lower(), phone_number = phone)

        return JsonResponse(objeto_success('¡El usuario fue agregado con éxito!', 'El usuario {} fue registrado exitosamente en la base de datos'.format(username), 'success', 'Aceptar'))

# Vista que procesa si las credenciales para iniciar sesión de un usuario son correctas
def procesarLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password_entered = request.POST['password']

        usuario = Usuario.objects.filter(username = username.lower())

        if usuario:
            if check_password(password_entered, usuario[0].hashed_salted_password):
                request.session['username'] = username
                return JsonResponse(objeto_success('¡Inicio de sesión exitoso!', 'Ha iniciado sesión como {}'.format(username).capitalize(), 'success', 'Aceptar'))

        return JsonResponse(objeto_error('username', '¡Credenciales incorrectas!', 'Las credenciales ingresadas son incorrectas. Intente de nuevo', 'error', 'Aceptar'))

# Vista para cerrar sesión en caso de existir una abierta
def logout(request):
    if 'username' in request.session:
        del request.session['username']
        return redirect('/')

# ======================================================
#                   SOLICITUD DE CITAS
# ======================================================

# Vista que renderiza el formulario de solicitar una cita y los elementos de las listas desplegables
def solicitarCita(request):
    nacionalidades = Nacionalidad.objects.all()
    motivos_consulta = MotivoDeConsulta.objects.all()
    sintomas = Sintoma.objects.all()
    doctores = Doctor.objects.all()
    urgencias = Urgencia.objects.all()
    sexos = Sexo.objects.all()
    necesidades_especiales = NecesidadEspecial.objects.all()
    parentescos = Parentesco.objects.all()
    contexto = {
        'nacionalidades': nacionalidades,
        'motivos': motivos_consulta,
        'sintomas': sintomas,
        'doctores': doctores,
        'urgencias': urgencias,
        'sexos': sexos,
        'necesidades': necesidades_especiales,
        'parentescos': parentescos
    }
    return render(request, 'secciones/solicitar-cita.html', contexto)

# Vista que procesa la solicitud de una cita
def procesarCita(request):
    if request.method == "POST":
        # Datos de la cita
        ci_cliente = request.POST['ciCliente']
        nacionalidad_cliente = request.POST['nacionalidadCliente']
        fecha_cita = request.POST['fechaCita']
        hora_cita = request.POST['horaCita']
        motivo_consulta = request.POST['motivoConsulta']
        sintomas = request.POST['sintomas'].split(",")
        doctor_cita = request.POST['doctorCita']
        urgencia = request.POST['urgencia']
        detalles = request.POST['detalles']
        primera_vez = request.POST['primeraVez']

        if not cedula_numero(ci_cliente):
            return JsonResponse(objeto_error('nci-cliente', 'Cédula inválida', 'La cédula de identidad del paciente debe ser un número entero', 'error', 'Corregir'))
        
        if not cedula_positiva(ci_cliente):
            return JsonResponse(objeto_error('nci-cliente', 'Cédula inválida', 'La cédula de identidad del paciente debe ser un número entero positivo', 'error', 'Corregir'))
        
        if not nacionalidad_correcta(nacionalidad_cliente):
            return JsonResponse(objeto_error('nacionalidad-cliente', 'Nacionalidad inválida', 'La nacionalidad del paciente ingresada es incorrecta', 'error', 'Corregir'))

        if not concordancia_nacionalidad(nacionalidad_cliente, ci_cliente):
            return JsonResponse(objeto_error('nacionalidad-cliente', 'Nacionalidad inválida', 'La cédula de identidad del paciente no coincide con su nacionalidad', 'warning', 'Cambiar'))

        if not fecha_correcta(fecha_cita):
            return JsonResponse(objeto_error('fecha-cita', 'Fecha inválida', 'La fecha de la cita ingresada es incorrecta o está en el formato incorrecto', 'error', 'Corregir'))

        if fecha_anterior_hoy(fecha_cita):
            return JsonResponse(objeto_error('fecha-cita', 'Fecha inválida', 'La fecha de la cita no puede ser anterior al día de hoy', 'error', 'Corregir'))

        if fecha_muy_a_futuro(fecha_cita):
            return JsonResponse(objeto_error('fecha-cita', 'Demasiada antelación', 'La fecha de la cita no puede tener una antelación mayor a un año', 'error', 'Corregir'))

        if not dia_semana_correcto(fecha_cita):
            return JsonResponse(objeto_error('fecha-cita', 'Fecha inválida', 'No se puede solicitar una cita para la fecha ingresada. La clínica sólo atiende los días lunes, miércoles y viernes', 'warning', 'Cambiar'))

        if not hora_correcta(hora_cita):
            return JsonResponse(objeto_error('hora-cita', 'Hora inválida', 'La hora de la cita ingresada es incorrecta o está en el formato incorrecto', 'error', 'Corregir'))

        if not horario_laboral(hora_cita):
            return JsonResponse(objeto_error('hora-cita', 'Hora inválida', 'La clínica trabaja de 8:30 a. m. a 3:30 p. m.', 'error', 'Cambiar'))

        if not intervalo_hora_correcto(hora_cita):
            return JsonResponse(objeto_error('hora-cita', 'Hora inválida', 'La hora de la cita ingresada es incorrecta. Solo se pueden solicitar citas para horas en punto', 'error', 'Cambiar'))

        if not valor_valido(motivo_consulta):
            return JsonResponse(objeto_error('motivo-consulta', 'Motivo desconocido', 'No se reconoce el motivo de la consulta', 'error', 'Corregir'))
        elif not MotivoDeConsulta.objects.filter(cod_motivo = motivo_consulta):
            return JsonResponse(objeto_error('motivo-consulta', 'Motivo desconocido', 'No se reconoce el motivo de la consulta', 'error', 'Corregir'))

        for sintoma in sintomas:
            if not valor_valido(sintoma):
                return JsonResponse(objeto_error('sintomas', 'Síntoma desconocido', 'No se reconoce uno de los síntomas del paciente', 'error', 'Corregir'))
            elif not Sintoma.objects.filter(cod_sintoma = sintoma):
                return JsonResponse(objeto_error('sintomas', 'Síntoma desconocido', 'No se reconoce uno de los síntomas del paciente', 'error', 'Corregir'))
            
        if not cedula_numero(doctor_cita):
            return JsonResponse(objeto_error('doctor-cita', 'Cédula incorrecta', 'La cédula de identidad del doctor debe ser un número entero', 'error', 'Corregir'))
        elif not cedula_positiva(doctor_cita):
            return JsonResponse(objeto_error('doctor-cita', 'Cédula incorrecta', 'La cédula de identidad del doctor debe ser un número entero positivo', 'error', 'Corregir'))
        elif not Doctor.objects.filter(ci_doctor = doctor_cita):
            return JsonResponse(objeto_error('doctor-cita', 'Doctor desconocido', 'No se encontró al doctor en la base de datos', 'error', 'Corregir'))

        if not valor_valido(urgencia):
            return JsonResponse(objeto_error('urgencia', 'Urgencia desconocida', 'No se reconoce la urgencia de la cita', 'error', 'Corregir'))
        elif not Urgencia.objects.filter(cod_urgencia = urgencia):
            return JsonResponse(objeto_error('urgencia', 'Urgencia desconocida', 'No se reconoce la urgencia de la cita', 'error', 'Corregir'))
        
        if campo_vacio(detalles):
            detalles = None
        elif solo_espacios_en_blanco(detalles):
            detalles = None
        
        if Cita.objects.filter(fecha = date.fromisoformat(fecha_cita), hora = datetime.strptime(hora_cita, "%H:%M")):
            return JsonResponse(objeto_error('fecha-cita', 'Fecha ocupada', 'Lo sentimos, esa fecha y hora ya están reservadas. Intente cambiar alguna de estas', 'warning', 'Cambiar'))
        
        if primera_vez == 'True':
            if Cliente.objects.filter(ci_cliente = ci_cliente):
                return JsonResponse(objeto_error('primera-vez-false', 'Paciente registrado', 'El paciente ya se encuentra registrado en la base de datos', 'error', 'Ocultar datos de registro'))

            # Datos del cliente
            nombres = request.POST['nombres']
            apellidos = request.POST['apellidos']
            fecha_nacimiento = request.POST['fechaNacimiento']
            sexo = request.POST['sexo']
            direccion = request.POST['direccion']
            necesidad_especial = request.POST['necesidadEspecial']
            telefonos = request.POST['telefonos'].split(",")
            emails = request.POST['emails'].split(",")
            tiene_parentesco = request.POST['tieneParentesco']

            if campo_vacio(nombres):
                return JsonResponse(objeto_error('nombres', 'Campo vacío', 'Debe completar el campo con los nombres', 'error', 'Completar'))

            if solo_espacios_en_blanco(nombres):
                return JsonResponse(objeto_error('nombres', 'Espacios en blanco', 'Los nombres no pueden estar compuestos sólo de espacios en blanco', 'error', 'Corregir'))

            if not comprobar_escritura(nombres):
                return JsonResponse(objeto_error('nombres', 'Nombres inválidos', 'Los nombres ingresados no cumplen con el estándar definido', 'error', 'Corregir'))
            
            if campo_vacio(apellidos):
                return JsonResponse(objeto_error('apellidos', 'Campo vacío', 'Debe completar el campo con los apellidos', 'error', 'Completar'))

            if solo_espacios_en_blanco(apellidos):
                return JsonResponse(objeto_error('apellidos', 'Espacios en blanco', 'Los apellidos no pueden estar compuestos sólo de espacios en blanco', 'error', 'Corregir'))

            if not comprobar_escritura(apellidos):
                return JsonResponse(objeto_error('apellidos', 'Apellidos inválidos', 'Los apellidos ingresados no cumplen con el estándar definido', 'error', 'Corregir'))

            if not fecha_correcta(fecha_nacimiento):
                return JsonResponse(objeto_error('fecha-de-nacimiento', 'Fecha inválida', 'La fecha de nacimiento ingresada es incorrecta o está en el formato incorrecto', 'error', 'Corregir'))

            if fecha_posterior_hoy(fecha_nacimiento):
                return JsonResponse(objeto_error('fecha-de-nacimiento', 'Fecha inválida', 'La fecha de nacimiento no puede ser posterior al día de hoy', 'error', 'Corregir'))

            if not mayor_de_edad(fecha_nacimiento):
                return JsonResponse(objeto_error('fecha-de-nacimiento', 'Eres menor de edad', 'Debes ser mayor de edad para solicitar una cita', 'error', 'Aceptar'))

            if es_centenario(fecha_nacimiento):
                return JsonResponse(objeto_error('fecha-de-nacimiento', 'Eres demasiado mayor', 'Usted es demasiado mayor para solicitar una cita', 'error', 'Aceptar'))

            if not valor_valido(sexo):
                return JsonResponse(objeto_error('sexo', 'Sexo inválido', 'No se reconoce el sexo ingresado', 'error', 'Corregir'))
            elif not Sexo.objects.filter(cod_sexo = sexo):
                return JsonResponse(objeto_error('sexo', 'Sexo inválido', 'No se reconoce el sexo ingresado', 'error', 'Corregir'))

            if campo_vacio(direccion):
                direccion = None
            elif solo_espacios_en_blanco(direccion):
                direccion = None

            if not valor_valido(necesidad_especial):
                return JsonResponse(objeto_error('necesidad-especial', 'Necesidad especial inválida', 'No se reconoce la necesidad especial ingresada', 'error', 'Corregir'))
            elif not NecesidadEspecial.objects.filter(cod_necesidad_especial = necesidad_especial):
                return JsonResponse(objeto_error('necesidad-especial', 'Necesidad especial inválida', 'No se reconoce la necesidad especial ingresada', 'error', 'Corregir'))
            
            if elementos_repetidos(telefonos):
                return JsonResponse(objeto_error('telefonos', 'Teléfonos repetidos', 'No se puede ingresar un mismo número de teléfono más de una vez', 'warning', 'Corregir'))

            for telefono in telefonos:
                if not phone_correcto(telefono):
                    return JsonResponse(objeto_error('telefonos', 'Teléfono inválido', 'Uno de los números de teléfono ingresados no cumple con el formato especificado', 'error', 'Corregir'))
                elif not Area.objects.filter(cod_area = telefono[:4]):
                    return JsonResponse(objeto_error('telefonos', 'Código de área inválido', 'No se reconoce el código de área de uno de los números de teléfono ingresados', 'warning', 'Corregir'))
                elif TelefonosClientes.objects.filter(area = telefono[:4], numero_telefonico = telefono[-7:]):
                    return JsonResponse(objeto_error('telefonos', 'Teléfono registrado', 'Uno de los números de teléfono ingresados ya se encuentra en uso. Intente nuevamente', 'warning', 'Corregir'))
            
            if elementos_repetidos(emails):
                return JsonResponse(objeto_error('emails', 'Correos electrónicos repetidos', 'No se puede ingresar un mismo correo electrónico más de una vez', 'warning', 'Corregir'))

            for email in emails:
                if not email_correcto(email):
                    return JsonResponse(objeto_error('emails', 'Correo electrónico inválido', 'Uno de los correos electrónicos ingresados no cumple con el formato especificado', 'error', 'Corregir'))
                elif not Dominio.objects.filter(descripcion_dominio = email[email.find("@"):]):
                    return JsonResponse(objeto_error('emails', 'Dominio web inválido', 'No se reconoce uno de los nombres de dominio de los correos electrónicos ingresados', 'warning', 'Corregir'))
                elif EmailsClientes.objects.filter(nombre_email = email.split("@")[0], dominio = Dominio.objects.filter(descripcion_dominio = email[email.find("@"):])[0].cod_dominio):
                    return JsonResponse(objeto_error('emails', 'Correo electrónico registrado', 'Uno de los correos electrónicos ingresados ya se encuentra en uso. Intente nuevamente', 'warning', 'Corregir'))
            
            if tiene_parentesco == 'True':
                ci_pariente = request.POST['ciPariente']
                nacionalidad_pariente = request.POST['nacionalidadPariente']
                parentesco = request.POST['parentesco']

                if not cedula_numero(ci_pariente):
                    return JsonResponse(objeto_error('nci-pariente', 'Cédula inválida', 'La cédula de identidad del pariente debe ser un número entero', 'error', 'Corregir'))
            
                if not cedula_positiva(ci_pariente):
                    return JsonResponse(objeto_error('nci-pariente', 'Cédula inválida', 'La cédula de identidad del pariente debe ser un número entero positivo', 'error', 'Corregir'))

                if not nacionalidad_correcta(nacionalidad_pariente):
                    return JsonResponse(objeto_error('nacionalidad-pariente', 'Nacionalidad inválida', 'La nacionalidad del pariente ingresada es incorrecta', 'error', 'Corregir'))

                if not concordancia_nacionalidad(nacionalidad_pariente, ci_pariente):
                    return JsonResponse(objeto_error('nacionalidad-pariente', 'Nacionalidad inválida', 'La cédula de identidad del pariente no coincide con su nacionalidad', 'warning', 'Cambiar'))
                
                if not valor_valido(parentesco):
                    return JsonResponse(objeto_error('parentesco', 'Parentesco inválido', 'No se reconoce el parentesco', 'error', 'Corregir'))
                elif not Parentesco.objects.filter(cod_parentesco = parentesco):
                    return JsonResponse(objeto_error('parentesco', 'Parentesco inválido', 'No se reconoce el parentesco', 'error', 'Corregir'))
                
                if not Cliente.objects.filter(ci_cliente = ci_pariente):
                    return JsonResponse(objeto_error('nci-pariente', 'Pariente no encontrado', 'La cédula de identidad del pariente indicado no se encuentra en la base de datos', 'error', 'Aceptar'))

            Cliente.objects.create(
                ci_cliente = int(ci_cliente),
                nacionalidad = Nacionalidad.objects.get(cod_nacionalidad = nacionalidad_cliente),
                nombres = nombres,
                apellidos = apellidos,
                fecha_nacimiento = date.fromisoformat(fecha_nacimiento),
                sexo = Sexo.objects.get(cod_sexo = int(sexo)),
                direccion = direccion,
                necesidad_especial = NecesidadEspecial.objects.get(cod_necesidad_especial = int(necesidad_especial))
            )

            for telefono in telefonos:
                TelefonosClientes.objects.create(
                    cliente = Cliente.objects.get(ci_cliente = int(ci_cliente)),
                    area = Area.objects.get(cod_area = telefono[:4]),
                    numero_telefonico = telefono[-7:]
                )
            
            for email in emails:
                nombre_destinatario = email.split("@")[0]
                dominio_completo = email[email.find("@"):]
                cod_dominio = Dominio.objects.filter(descripcion_dominio = dominio_completo)[0].cod_dominio
                EmailsClientes.objects.create(
                    cliente = Cliente.objects.get(ci_cliente = int(ci_cliente)),
                    nombre_email = nombre_destinatario,
                    dominio = Dominio.objects.get(cod_dominio = int(cod_dominio))
                )
            
            if tiene_parentesco == 'True':
                Familiar.objects.create(
                    nuevo_paciente = Cliente.objects.get(ci_cliente = int(ci_cliente)),
                    familiar = Cliente.objects.get(ci_cliente = int(ci_pariente)),
                    parentesco = Parentesco.objects.get(cod_parentesco = int(parentesco))
                )

        if not Cliente.objects.filter(ci_cliente = ci_cliente):
            return JsonResponse(objeto_error('primera-vez-true', 'Paciente no encontrado', 'El paciente ingresado no se encontró en la base de datos', 'error', 'Abrir datos de registro'))

        Cita.objects.create(
            cliente = Cliente.objects.get(ci_cliente = int(ci_cliente)),
            fecha = date.fromisoformat(fecha_cita),
            hora = datetime.strptime(hora_cita, "%H:%M"),
            motivo = MotivoDeConsulta.objects.get(cod_motivo = int(motivo_consulta)),
            doctor_cita = Doctor.objects.get(ci_doctor = int(doctor_cita)),
            urgencia = Urgencia.objects.get(cod_urgencia = int(urgencia)),
            detalles = detalles
        )

        for sintoma in sintomas:
            SintomasCita.objects.create(
                cita = Cita.objects.get(fecha = date.fromisoformat(fecha_cita), hora = datetime.strptime(hora_cita, "%H:%M")),
                sintoma = Sintoma.objects.get(cod_sintoma = int(sintoma))
            )
        
        return JsonResponse(objeto_success('¡Solicitud exitosa!', '¡La cita fue solicitada con éxito!', 'success', 'Aceptar'))

# ============================================================
#                     ADMINISTRAR DOCTORES
# ============================================================

# Vista que renderiza la página de administración de los doctores
def administrarDoctores(request):
    if 'username' in request.session:
        doctores = Doctor.objects.all()
        contexto = {
            'doctores': doctores
        }
        return render(request, 'administrar/administrar-doctores.html', contexto)

# Vista que renderiza el formulario para agregar a un doctor con sus listas desplegables
def agregarDoctor(request):
    if 'username' in request.session:
        nacionalidades = Nacionalidad.objects.all()
        sexos = Sexo.objects.all()
        especialidades = Especialidad.objects.all()
        contexto = {
            'nacionalidades': nacionalidades,
            'sexos': sexos,
            'especialidades': especialidades
        }
        return render(request, 'administrar/agregar-doctor.html', contexto)

# Vista que procesa los datos personales del doctor y lo registra en caso de ser correctos
def registrarDoctor(request):
    if 'username' in request.session:
        if request.method == 'POST':
            ci_doctor = request.POST['ciDoctor']
            nacionalidad_doctor = request.POST['nacionalidadDoctor']
            nombres = request.POST['nombres']
            apellidos = request.POST['apellidos']
            fecha_nacimiento = request.POST['fechaNacimiento']
            sexo = request.POST['sexo']
            direccion = request.POST['direccion']
            especialidad = request.POST['especialidad']
            telefonos = request.POST['telefonos'].split(",")
            emails = request.POST['emails'].split(",")

            if not cedula_numero(ci_doctor):
                return JsonResponse(objeto_error('nci-doctor', 'Cédula inválida', 'La cédula de identidad del doctor debe ser un número entero', 'error', 'Corregir'))
        
            if not cedula_positiva(ci_doctor):
                return JsonResponse(objeto_error('nci-doctor', 'Cédula inválida', 'La cédula de identidad del doctor debe ser un número entero positivo', 'error', 'Corregir'))

            if Doctor.objects.filter(ci_doctor = ci_doctor):
                return JsonResponse(objeto_error('nci-doctor', 'Doctor registrado', 'El doctor ya se encuentra registrado en la base de datos', 'error', 'Aceptar'))
            
            if not nacionalidad_correcta(nacionalidad_doctor):
                return JsonResponse(objeto_error('nacionalidad-doctor', 'Nacionalidad inválida', 'La nacionalidad del doctor ingresada es incorrecta', 'error', 'Corregir'))

            if not concordancia_nacionalidad(nacionalidad_doctor, ci_doctor):
                return JsonResponse(objeto_error('nacionalidad-doctor', 'Nacionalidad inválida', 'La cédula de identidad del doctor no coincide con su nacionalidad', 'warning', 'Cambiar'))
            
            if campo_vacio(nombres):
                return JsonResponse(objeto_error('nombres', 'Campo vacío', 'Debe completar el campo con los nombres', 'error', 'Completar'))

            if solo_espacios_en_blanco(nombres):
                return JsonResponse(objeto_error('nombres', 'Espacios en blanco', 'Los nombres no pueden estar compuestos sólo de espacios en blanco', 'error', 'Corregir'))

            if not comprobar_escritura(nombres):
                return JsonResponse(objeto_error('nombres', 'Nombres inválidos', 'Los nombres ingresados no cumplen con el estándar definido', 'error', 'Corregir'))
            
            if campo_vacio(apellidos):
                return JsonResponse(objeto_error('apellidos', 'Campo vacío', 'Debe completar el campo con los apellidos', 'error', 'Completar'))

            if solo_espacios_en_blanco(apellidos):
                return JsonResponse(objeto_error('apellidos', 'Espacios en blanco', 'Los apellidos no pueden estar compuestos sólo de espacios en blanco', 'error', 'Corregir'))

            if not comprobar_escritura(apellidos):
                return JsonResponse(objeto_error('apellidos', 'Apellidos inválidos', 'Los apellidos ingresados no cumplen con el estándar definido', 'error', 'Corregir'))

            if not fecha_correcta(fecha_nacimiento):
                return JsonResponse(objeto_error('fecha-de-nacimiento', 'Fecha inválida', 'La fecha de nacimiento ingresada es incorrecta o está en el formato incorrecto', 'error', 'Corregir'))

            if fecha_posterior_hoy(fecha_nacimiento):
                return JsonResponse(objeto_error('fecha-de-nacimiento', 'Fecha inválida', 'La fecha de nacimiento no puede ser posterior al día de hoy', 'error', 'Corregir'))

            if not mayor_de_edad(fecha_nacimiento):
                return JsonResponse(objeto_error('fecha-de-nacimiento', 'Eres menor de edad', 'Debes ser mayor de edad para ejercer la odontología', 'error', 'Aceptar'))

            if es_centenario(fecha_nacimiento):
                return JsonResponse(objeto_error('fecha-de-nacimiento', 'Eres demasiado mayor', 'Usted es demasiado mayor para ejercer la odontología', 'error', 'Aceptar'))

            if not valor_valido(sexo):
                return JsonResponse(objeto_error('sexo', 'Sexo inválido', 'No se reconoce el sexo ingresado', 'error', 'Corregir'))
            elif not Sexo.objects.filter(cod_sexo = sexo):
                return JsonResponse(objeto_error('sexo', 'Sexo inválido', 'No se reconoce el sexo ingresado', 'error', 'Corregir'))

            if campo_vacio(direccion):
                direccion = None
            elif solo_espacios_en_blanco(direccion):
                direccion = None
            
            if not valor_valido(especialidad):
                return JsonResponse(objeto_error('especialidad', 'Especialidad inválida', 'No se reconoce la especialidad ingresada', 'error', 'Corregir'))
            elif not Especialidad.objects.filter(cod_especialidad = especialidad):
                return JsonResponse(objeto_error('especialidad', 'Especialidad inválida', 'No se reconoce la especialidad ingresada', 'error', 'Corregir'))

            if elementos_repetidos(telefonos):
                return JsonResponse(objeto_error('telefonos', 'Teléfonos repetidos', 'No se puede ingresar un mismo número de teléfono más de una vez', 'warning', 'Corregir'))

            for telefono in telefonos:
                if not phone_correcto(telefono):
                    return JsonResponse(objeto_error('telefonos', 'Teléfono inválido', 'Uno de los números de teléfono ingresados no cumple con el formato especificado', 'error', 'Corregir'))
                elif not Area.objects.filter(cod_area = telefono[:4]):
                    return JsonResponse(objeto_error('telefonos', 'Código de área inválido', 'No se reconoce el código de área de uno de los números de teléfono ingresados', 'warning', 'Corregir'))
                elif TelefonosDoctores.objects.filter(area = telefono[:4], numero_telefonico = telefono[-7:]):
                    return JsonResponse(objeto_error('telefonos', 'Teléfono registrado', 'Uno de los números de teléfono ingresados ya se encuentra en uso. Intente nuevamente', 'warning', 'Corregir'))
            
            if elementos_repetidos(emails):
                return JsonResponse(objeto_error('emails', 'Correos electrónicos repetidos', 'No se puede ingresar un mismo correo electrónico más de una vez', 'warning', 'Corregir'))

            for email in emails:
                if not email_correcto(email):
                    return JsonResponse(objeto_error('emails', 'Correo electrónico inválido', 'Uno de los correos electrónicos ingresados no cumple con el formato especificado', 'error', 'Corregir'))
                elif not Dominio.objects.filter(descripcion_dominio = email[email.find("@"):]):
                    return JsonResponse(objeto_error('emails', 'Dominio web inválido', 'No se reconoce uno de los nombres de dominio de los correos electrónicos ingresados', 'warning', 'Corregir'))
                elif EmailsDoctores.objects.filter(nombre_email = email.split("@")[0], dominio = Dominio.objects.filter(descripcion_dominio = email[email.find("@"):])[0].cod_dominio):
                    return JsonResponse(objeto_error('emails', 'Correo electrónico registrado', 'Uno de los correos electrónicos ingresados ya se encuentra en uso. Intente nuevamente', 'warning', 'Corregir'))
            
            Doctor.objects.create(
                ci_doctor = int(ci_doctor),
                nacionalidad = Nacionalidad.objects.get(cod_nacionalidad = nacionalidad_doctor),
                nombres = nombres,
                apellidos = apellidos,
                fecha_nacimiento = date.fromisoformat(fecha_nacimiento),
                sexo = Sexo.objects.get(cod_sexo = int(sexo)),
                direccion = direccion,
                especialidad = Especialidad.objects.get(cod_especialidad = int(especialidad))
            )

            for telefono in telefonos:
                TelefonosDoctores.objects.create(
                    doctor = Doctor.objects.get(ci_doctor = int(ci_doctor)),
                    area = Area.objects.get(cod_area = telefono[:4]),
                    numero_telefonico = telefono[-7:]
                )
            
            for email in emails:
                nombre_destinatario = email.split("@")[0]
                dominio_completo = email[email.find("@"):]
                cod_dominio = Dominio.objects.filter(descripcion_dominio = dominio_completo)[0].cod_dominio
                EmailsDoctores.objects.create(
                    doctor = Doctor.objects.get(ci_doctor = int(ci_doctor)),
                    nombre_email = nombre_destinatario,
                    dominio = Dominio.objects.get(cod_dominio = int(cod_dominio))
                )
            
            primer_nombre = nombres.split(" ")[0]

            if int(sexo) == 1:
                success = '¡La doctora {} fue registrada con éxito!'.format(primer_nombre)
            elif int(sexo) == 2:
                success = '¡El doctor {} fue registrado con éxito!'.format(primer_nombre)
            else:
                success = '¡El registro fue realizado con éxito!'

            return JsonResponse(objeto_success('¡Registro exitoso!', success, 'success', 'Aceptar'))

# Vista que renderiza el formulario para actualizar los datos personales de un doctor
def actualizarDoctor(request, ci_doctor):
    if 'username' in request.session:
        nacionalidades = Nacionalidad.objects.all()
        sexos = Sexo.objects.all()
        especialidades = Especialidad.objects.all()
        doctor = Doctor.objects.get(ci_doctor = ci_doctor)
        contexto = {
            'nacionalidades': nacionalidades,
            'sexos': sexos,
            'especialidades': especialidades,
            'doctor': doctor
        }
        return render(request, 'administrar/actualizar-doctor.html', contexto)

# Vista que procesa los cambios hechos a los datos personales de un doctor
def cambiarDoctor(request):
    if 'username' in request.session:
        if request.method == 'POST':
            ci_doctor = request.POST['ciDoctor']
            nombres = request.POST['nombres']
            apellidos = request.POST['apellidos']
            direccion = request.POST['direccion']
            especialidad = request.POST['especialidad']
            telefonos = request.POST['telefonos'].split(",")
            emails = request.POST['emails'].split(",")

            if not cedula_numero(ci_doctor):
                return JsonResponse(objeto_error('nci-doctor', 'Cédula inválida', 'La cédula de identidad del doctor debe ser un número entero', 'error', 'Corregir'))
        
            if not cedula_positiva(ci_doctor):
                return JsonResponse(objeto_error('nci-doctor', 'Cédula inválida', 'La cédula de identidad del doctor debe ser un número entero positivo', 'error', 'Corregir'))

            if not Doctor.objects.filter(ci_doctor = ci_doctor):
                return JsonResponse(objeto_error('nci-doctor', 'Doctor no encontrado', 'El doctor ingresado no se encuentra registrado en la base de datos', 'error', 'Aceptar'))
            
            if campo_vacio(nombres):
                return JsonResponse(objeto_error('nombres', 'Campo vacío', 'Debe completar el campo con los nombres', 'error', 'Completar'))

            if solo_espacios_en_blanco(nombres):
                return JsonResponse(objeto_error('nombres', 'Espacios en blanco', 'Los nombres no pueden estar compuestos sólo de espacios en blanco', 'error', 'Corregir'))

            if not comprobar_escritura(nombres):
                return JsonResponse(objeto_error('nombres', 'Nombres inválidos', 'Los nombres ingresados no cumplen con el estándar definido', 'error', 'Corregir'))
            
            if campo_vacio(apellidos):
                return JsonResponse(objeto_error('apellidos', 'Campo vacío', 'Debe completar el campo con los apellidos', 'error', 'Completar'))

            if solo_espacios_en_blanco(apellidos):
                return JsonResponse(objeto_error('apellidos', 'Espacios en blanco', 'Los apellidos no pueden estar compuestos sólo de espacios en blanco', 'error', 'Corregir'))

            if not comprobar_escritura(apellidos):
                return JsonResponse(objeto_error('apellidos', 'Apellidos inválidos', 'Los apellidos ingresados no cumplen con el estándar definido', 'error', 'Corregir'))

            if campo_vacio(direccion):
                direccion = None
            elif solo_espacios_en_blanco(direccion):
                direccion = None
            
            if not valor_valido(especialidad):
                return JsonResponse(objeto_error('especialidad', 'Especialidad inválida', 'No se reconoce la especialidad ingresada', 'error', 'Corregir'))
            elif not Especialidad.objects.filter(cod_especialidad = especialidad):
                return JsonResponse(objeto_error('especialidad', 'Especialidad inválida', 'No se reconoce la especialidad ingresada', 'error', 'Corregir'))

            # Si el usuario desea cambiar un número de teléfono, es decir, si no deja el espacio en blanco
            if telefonos[0]:
                if elementos_repetidos(telefonos):
                    return JsonResponse(objeto_error('telefonos', 'Teléfonos repetidos', 'No se puede ingresar un mismo número de teléfono más de una vez', 'warning', 'Corregir'))

                for telefono in telefonos:
                    if not phone_correcto(telefono):
                        return JsonResponse(objeto_error('telefonos', 'Teléfono inválido', 'Uno de los números de teléfono ingresados no cumple con el formato especificado', 'error', 'Corregir'))
                    elif not Area.objects.filter(cod_area = telefono[:4]):
                        return JsonResponse(objeto_error('telefonos', 'Código de área inválido', 'No se reconoce el código de área de uno de los números de teléfono ingresados', 'warning', 'Corregir'))
                    elif TelefonosDoctores.objects.filter(area = telefono[:4], numero_telefonico = telefono[-7:]):
                        return JsonResponse(objeto_error('telefonos', 'Teléfono registrado', 'Uno de los números de teléfono ingresados ya se encuentra en uso. Intente nuevamente', 'warning', 'Corregir'))
            
            # Si el usuario desea cambiar un correo electrónico, es decir, si no deja el espacio en blanco
            if emails[0]:
                if elementos_repetidos(emails):
                    return JsonResponse(objeto_error('emails', 'Correos electrónicos repetidos', 'No se puede ingresar un mismo correo electrónico más de una vez', 'warning', 'Corregir'))

                for email in emails:
                    if not email_correcto(email):
                        return JsonResponse(objeto_error('emails', 'Correo electrónico inválido', 'Uno de los correos electrónicos ingresados no cumple con el formato especificado', 'error', 'Corregir'))
                    elif not Dominio.objects.filter(descripcion_dominio = email[email.find("@"):]):
                        return JsonResponse(objeto_error('emails', 'Dominio web inválido', 'No se reconoce uno de los nombres de dominio de los correos electrónicos ingresados', 'warning', 'Corregir'))
                    elif EmailsDoctores.objects.filter(nombre_email = email.split("@")[0], dominio = Dominio.objects.filter(descripcion_dominio = email[email.find("@"):])[0].cod_dominio):
                        return JsonResponse(objeto_error('emails', 'Correo electrónico registrado', 'Uno de los correos electrónicos ingresados ya se encuentra en uso. Intente nuevamente', 'warning', 'Corregir'))

            # Se obtienen los datos del doctor que se desean modificar
            doctor = Doctor.objects.get(ci_doctor = ci_doctor)
            # Se modifican los datos del doctor
            doctor.nombres = nombres
            doctor.apellidos = apellidos
            doctor.direccion = direccion
            doctor.especialidad = Especialidad.objects.get(cod_especialidad = especialidad)
            doctor.save()

            if telefonos[0]:
                TelefonosDoctores.objects.filter(doctor = doctor).delete()

                for telefono in telefonos:
                    TelefonosDoctores.objects.create(
                        doctor = Doctor.objects.get(ci_doctor = int(ci_doctor)),
                        area = Area.objects.get(cod_area = telefono[:4]),
                        numero_telefonico = telefono[-7:]
                    )
            if emails[0]:
                EmailsDoctores.objects.filter(doctor = doctor).delete()

                for email in emails:
                    nombre_destinatario = email.split("@")[0]
                    dominio_completo = email[email.find("@"):]
                    cod_dominio = Dominio.objects.filter(descripcion_dominio = dominio_completo)[0].cod_dominio
                    EmailsDoctores.objects.create(
                        doctor = Doctor.objects.get(ci_doctor = int(ci_doctor)),
                        nombre_email = nombre_destinatario,
                        dominio = Dominio.objects.get(cod_dominio = int(cod_dominio))
                    )
            doctor.save()

            return JsonResponse(objeto_success('¡Actualización exitosa!', 'Los cambios de los datos personales fueron realizados con éxito', 'success', 'Aceptar'))

# Vista que procesa la eliminación de un doctor de la base de datos
def despedirDoctor(request, ci_doctor):
    if 'username' in request.session:
        doctor = Doctor.objects.get(ci_doctor = ci_doctor)
        doctor.delete()

        return redirect('administrar/administrar-doctores')

# ===================================================
#                  ADMINISTRAR CITAS
# ===================================================

# Vista que renderiza la página de administración de citas y que muestra los datos de las tablas
def administrarCitas(request):
    if 'username' in request.session:
        hoy = date.today()
        citas = Cita.objects.filter(cita_aceptada = None,  fecha__gte = hoy)
        citas_aceptadas = CitaAceptada.objects.filter(cita__fecha__gte = hoy)
        citas_rechazadas = CitaRechazada.objects.filter(cita__fecha__gte = hoy)
        contexto = {
            'citas': citas,
            'citas_aceptadas': citas_aceptadas,
            'citas_rechazadas': citas_rechazadas
        }
        return render(request, 'administrar/administrar-citas.html', contexto)

# Vista que procesa cuando una cita es aceptada y envia un correo electrónico al paciente
def aceptarCita(request, id_cita):
    if 'username' in request.session:
        cita = Cita.objects.get(id_cita = id_cita)
        cita.cita_aceptada = True
        cita.save()
        CitaAceptada.objects.create(cita = cita)

        correo_cliente = EmailsClientes.objects.get(cliente = cita.cliente)
        fecha_cita = format_date(cita.fecha, "EEEE, dd 'de' MMMM 'de' YYYY", 'es_VE').capitalize()
        hora_cita = format_time(cita.hora, 'hh:mm a')

        # Datos para enviar un correo electrónico de confirmación
        destinatario = correo_cliente.nombre_email + correo_cliente.dominio.descripcion_dominio
        asunto = 'Solicitud de cita aceptada'
        para = cita.cliente.apellidos + ", " + cita.cliente.nombres
        mensaje = 'Estimado cliente, la presente tiene como propósito informarle que la cita que solicitó para el día {} a las {} ha sido aceptada. Muchas gracias por su preferencia y esperamos poder verle en la fecha acordada. Para más información, no dude en contactárnos a través de nuestro correo electrónico o por medio de WhatsApp. Le deseamos un excelente día.'.format(fecha_cita, hora_cita)
        enviar_email(destinatario, asunto, para, mensaje)

        return redirect('administrarCitas')

# Vista que procesa cuando una cita es rechazada y envia un correo electrónico al paciente
def rechazarCita(request, id_cita):
    if 'username' in request.session:
        cita = Cita.objects.get(id_cita = id_cita)
        cita.cita_aceptada = False
        cita.save()
        CitaRechazada.objects.create(cita = cita)

        correo_cliente = EmailsClientes.objects.get(cliente = cita.cliente)
        fecha_cita = format_date(cita.fecha, "EEEE, dd 'de' MMMM 'de' YYYY", 'es_VE').capitalize()
        hora_cita = format_time(cita.hora, 'hh:mm a')

        # Datos para enviar un correo electrónico de rechazo
        destinatario = correo_cliente.nombre_email + correo_cliente.dominio.descripcion_dominio
        asunto = 'Solicitud de cita rechazada'
        para = cita.cliente.apellidos + ", " + cita.cliente.nombres
        mensaje = 'Estimado cliente, la presente tiene como propósito informarle que, lamentablemente, la cita que solicitó para el día {} a las {} ha sido rechazada. Para más información, no dude en contactárnos a través de nuestro correo electrónico o por medio de WhatsApp. Muchas gracias por su preferencia y esperamos poder verle en otra ocasión. Le deseamos un excelente día.'.format(fecha_cita, hora_cita)
        enviar_email(destinatario, asunto, para, mensaje)

        return redirect('administrarCitas')

# Vista que renderiza la página de modificación de una cita aceptada con sus listas desplegables
def modificarCitaAceptada(request, id_cita):
    if 'username' in request.session:
        cita = Cita.objects.get(id_cita = id_cita)
        cita_aceptada = CitaAceptada.objects.get(cita = cita)
        doctores = Doctor.objects.all()
        diagnosticos = Diagnostico.objects.all()
        motivos_ausencia = MotivoDeAusencia.objects.all()
        contexto = {
            'cita_aceptada': cita_aceptada,
            'doctores': doctores,
            'diagnosticos': diagnosticos,
            'motivos_ausencia': motivos_ausencia
        }
        return render(request, 'administrar/modificar-cita-aceptada.html', contexto)

# Vista que procesa los cambios en una cita aceptada (doctor, diagnóstico, etc.)
def cambiarCitaAceptada(request):
    if 'username' in request.session:
        if request.method == 'POST':
            id_cita = request.POST['id_cita']
            doctor = request.POST['doctor']
            diagnostico = request.POST['diagnostico']
            cita_cumplida = request.POST.get('cita-cumplida')
            motivo_ausencia = request.POST['ausencia']

            cita = Cita.objects.get(id_cita = id_cita)
            cita_aceptada = CitaAceptada.objects.get(cita = cita)

            if doctor:
                cita_aceptada.doctor = Doctor.objects.get(ci_doctor = doctor)
            else:
                cita_aceptada.doctor = None

            if diagnostico:
                cita_aceptada.diagnostico = Diagnostico.objects.get(cod_diagnostico = diagnostico)
            else:
                cita_aceptada.diagnostico = None

            if cita_cumplida == 'True':
                cita_aceptada.cita_cumplida = True
                cita_aceptada.ausencia = None
            elif cita_cumplida == 'False':
                cita_aceptada.cita_cumplida = False
                if motivo_ausencia:
                    cita_aceptada.ausencia = MotivoDeAusencia.objects.get(cod_ausencia = motivo_ausencia)
                else:
                    cita_aceptada.ausencia = None
            else:
                cita_aceptada.cita_cumplida = None
                cita_aceptada.ausencia = None

            cita_aceptada.save()

            return redirect('administrarCitas')

# Vista que procesa cuando una cita es cancelada y envia un correo electrónico al paciente
def quitarCitaAceptada(request, id_cita):
    if 'username' in request.session:
        cita = Cita.objects.get(id_cita = id_cita)
        cita.cita_aceptada = None
        cita.save()

        correo_cliente = EmailsClientes.objects.get(cliente = cita.cliente)
        fecha_cita = format_date(cita.fecha, "EEEE, dd 'de' MMMM 'de' YYYY", 'es_VE').capitalize()
        hora_cita = format_time(cita.hora, 'hh:mm a')

        # Datos para enviar un correo electrónico de cancelación
        destinatario = correo_cliente.nombre_email + correo_cliente.dominio.descripcion_dominio
        asunto = 'Cita cancelada'
        para = cita.cliente.apellidos + ", " + cita.cliente.nombres
        mensaje = 'Estimado cliente, la presente tiene como propósito informarle que, lamentablemente, su cita anteriormente agendada para el día {} a las {} ha sido cancelada. Para más información, no dude en contactárnos a través de nuestro correo electrónico o por medio de WhatsApp. Muchas gracias por su preferencia y lamentamos los inconvenientes que hayamos podido causar. Le deseamos un excelente día.'.format(fecha_cita, hora_cita)
        enviar_email(destinatario, asunto, para, mensaje)

        CitaAceptada.objects.get(cita = cita).delete()

        return redirect('administrarCitas')

# Vista que procesa cuando se quita una cita de la lista de citas rechazadas
def quitarCitaRechazada(request, id_cita):
    if 'username' in request.session:
        cita = Cita.objects.get(id_cita = id_cita)
        cita.cita_aceptada = None
        cita.save()

        CitaRechazada.objects.get(cita = cita).delete()

        return redirect('administrarCitas')

# ================================================
#                 VISUALIZAR DATOS
# ================================================

# Vista que renderiza los detalles de una cita específica
def verCita(request, id_cita):
    if 'username' in request.session:
        cita = Cita.objects.get(id_cita = id_cita)
        sintomas_cita = SintomasCita.objects.filter(cita = cita)
        cita_aceptada = CitaAceptada.objects.filter(cita = cita)
        contexto = {
            'cita': cita,
            'sintomas_cita': sintomas_cita
        }
        if cita_aceptada:
            contexto['cita_aceptada'] = cita_aceptada[0]
        return render(request, 'administrar/ver-cita.html', contexto)

# Vista que renderiza los datos personales de un cliente específico
def verCliente(request, ci_cliente):
    if 'username' in request.session:
        cliente = Cliente.objects.get(ci_cliente = ci_cliente)
        telefonos_cliente = TelefonosClientes.objects.filter(cliente = cliente)
        emails_cliente = EmailsClientes.objects.filter(cliente = cliente)
        familiar = Familiar.objects.filter(nuevo_paciente = cliente)
        contexto = {
            'cliente': cliente,
            'telefonos_cliente': telefonos_cliente,
            'emails_cliente': emails_cliente
        }
        if familiar:
            contexto['familiar'] = familiar[0]
        return render(request, 'administrar/ver-cliente.html', contexto)

# Vista que renderiza los datos personales de un doctor específico
def verDoctor(request, ci_doctor):
    if 'username' in request.session:
        doctor = Doctor.objects.get(ci_doctor = ci_doctor)
        telefonos_doctor = TelefonosDoctores.objects.filter(doctor = doctor)
        emails_doctor = EmailsDoctores.objects.filter(doctor = doctor)
        contexto = {
            'doctor': doctor,
            'telefonos_doctor': telefonos_doctor,
            'emails_doctor': emails_doctor
        }
        return render(request, 'administrar/ver-doctor.html', contexto)
