from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import re

# Librería con funciones para validar que los datos ingresados sean correctos

# Función que revisa si el campo ingresado está vacío
def campo_vacio(cadena):
    if len(cadena) == 0:
        return True
    else:
        return False

# Función que revisa si el campo ingresado está compuesto solo de espacios en blanco
def solo_espacios_en_blanco(cadena):
    if cadena.isspace():
        return True
    else:
        return False

# Función que revisa si la longitud del nombre de usuario es correcta
def longitud_username_correcta(username):
    if len(username) >= 6 and len(username) <= 30:
        return True
    else:
        return False

# Función que revisa si el campo ingresado contiene espacios en blanco
def tiene_espacios_en_blanco(cadena):
    if ' ' in cadena:
        return True
    else:
        return False
    
# Función que revisa si el nombre de usuario contiene caracteres especiales, aparte del punto '.'
def tiene_caracteres_especiales(username):
    regex = r"[a-zA-Z0-9.]{6,30}"
    if re.fullmatch(regex, username):
        return False
    else:
        return True

# Función que revisa si el nombre de usuario inicia o termina con un punto
def inicia_termina_con_punto(username):
    if username[0] == '.' or username[-1] == '.':
        return True
    else:
        return False

# Función que revisa si el nombre de usuario contiene dos puntos '..' consecutivos
def dos_puntos_consecutivos(username):
    if '..' in username:
        return True
    else:
        return False

# Función que revisa si la longitud de la contraseña es correcta
def longitud_password_correcta(password):
    if len(password) >= 14 and len(password) <= 127:
        return True
    else:
        return False

# Función que revisa si la contraseña contiene mayúsculas, mínusculas, números y al menos un caracter especial
def password_segura(password):
    if not re.search('[a-z]', password):
        return False
    elif not re.search('[A-Z]', password):
        return False
    elif not re.search('[0-9]', password):
        return False
    elif not re.search("[._+!#$%&/='?*`}{|\^-]", password):
        return False
    return True

# Función para revisar si hay elementos repetidos en una lista
def elementos_repetidos(lista):
    i = 0
    j = 0
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

# Función para revisar si una cadena tiene dos caracteres especiales consecutivos
def caracter_duplicado(cadena):
    caracteres_especiales = [".", "^", "_", "+", "!", "#", "$", "%", "&", "/", "=", "'", "?", "*", "`", "}", "{", "|", "-"]
    for i in range(len(cadena) - 1):
        if cadena[i] == cadena[i + 1] and cadena[i] in caracteres_especiales:
            return True
    return False

# Función que revisa si el correo electrónico cumple con el formato especificado
def email_correcto(email):
    regex = r"[a-zA-Z0-9.^_+!#$%&/='?*`}{|-]{1,64}[@][a-zA-Z0-9.-]{1,253}[.][a-z]{2,18}"
    caracteres_especiales = [".", "^", "_", "+", "!", "#", "$", "%", "&", "/", "=", "'", "?", "*", "`", "}", "{", "|", "-"]

    try:
        nombre_destinatario = email.split("@")[0]
        nombre_dominio = email.split("@")[1][:email.split("@")[1].rfind(".")]
    except IndexError:
        return False

    if not (re.fullmatch(regex, email)):
        return False
    elif nombre_destinatario[0] in caracteres_especiales or nombre_destinatario[-1] in caracteres_especiales:
        return False
    elif caracter_duplicado(nombre_destinatario):
        return False
    elif nombre_dominio[0] in [".", "-"] or nombre_dominio[-1] in [".", "-"]:
        return False
    elif nombre_dominio[2:4] == "--":
        return False
    return True

# Función para revisar si el número de teléfono cumple con el formato especificado
def phone_correcto(phone):
    regex = r"[0][0-9]{3}[-][0-9]{7}"
    if not (re.fullmatch(regex, phone)):
        return False
    else:
        return True

# Función que revisa si la cédula de identidad introducida es un número
def cedula_numero(nci):
    try:
        int(nci)
        return True
    except ValueError:
        return False

# Función que revisa si la cédula es un número entero positivo
def cedula_positiva(nci):
    if int(nci) > 0:
        return True
    else:
        return False

# Función que revisa si la nacionalidad ingresada es correcta
def nacionalidad_correcta(nacionalidad):
    try:
        if nacionalidad.upper() == "V" or nacionalidad.upper() == "E":
            return True
        else:
            return False
    except AttributeError:
        return False

# Función que revisa si el número de cédula concuerda con la nacionalidad
def concordancia_nacionalidad(nacionalidad, nci):
    if nacionalidad == "V" and int(nci) < 80000000:
        return True
    elif nacionalidad == "E" and int(nci) >= 80000000:
        return True
    else:
        return False

# Función para comprobar la escritura correcta de nombres y apellidos
def comprobar_escritura(cadena):
    regex = r'[a-zA-ZÀ-ž\s]{3,60}'
    if len(cadena) < 3 or len(cadena) > 60:
        return False
    elif not (re.fullmatch(regex, cadena)):
        return False
    return True

# Función que revisa si una fecha ingresada es correcta
def fecha_correcta(cadena_fecha):
    try:
        date.fromisoformat(cadena_fecha)
        return True
    except (TypeError, ValueError):
        return False

# Función que revisa si la fecha ingresada es posterior al día de hoy
def fecha_posterior_hoy(cadena_fecha):
    fecha = date.fromisoformat(cadena_fecha)
    if fecha >= date.today():
        return True
    else:
        return False

# Función que revisa si la fecha ingresada es anterior al día de hoy
def fecha_anterior_hoy(cadena_fecha):
    fecha = date.fromisoformat(cadena_fecha)
    if fecha < date.today():
        return True
    else:
        return False

# Función que revisa si la fecha ingresada para la cita tiene más de un año de antelación
def fecha_muy_a_futuro(cadena_fecha):
    fecha_cita = date.fromisoformat(cadena_fecha)
    if fecha_cita > date.today() + relativedelta(years=1):
        return True
    else:
        return False

# Función que revisa si la fecha ingresada para la cita es un día de la semana correcto: lunes, miércoles o viernes
def dia_semana_correcto(cadena_fecha):
    fecha = date.fromisoformat(cadena_fecha)
    if fecha.isoweekday() == 1 or fecha.isoweekday() == 3 or fecha.isoweekday() == 5:
        return True
    else:
        return False

# Función que revisa si una persona es mayor de edad
def mayor_de_edad(cadena_fecha):
    fecha_nacimiento = date.fromisoformat(cadena_fecha)
    if fecha_nacimiento <= date.today() - relativedelta(years=18):
        return True
    else:
        return False

# Función que revisa si una persona tiene más de 100 años de edad
def es_centenario(cadena_fecha):
    fecha_nacimiento = date.fromisoformat(cadena_fecha)
    if fecha_nacimiento <= date.today() - relativedelta(years=100):
        return True
    else:
        return False

# Función que revisa si una hora ingresada es correcta
def hora_correcta(cadena_hora):
    try:
        datetime.strptime(cadena_hora, "%H:%M")
        return True
    except (TypeError, ValueError):
        return False

# Función que revisa si una hora ingresada está dentro del horario laboral
def horario_laboral(cadena_hora):
    hora = datetime.strptime(cadena_hora, "%H:%M")
    if hora < datetime.strptime("08:30", "%H:%M"):
        return False
    elif hora > datetime.strptime("15:30", "%H:%M"):
        return False
    else:
        return True

# Función que revisa si el intervalo entre las horas es correcto
def intervalo_hora_correcto(cadena_hora):
    hora = datetime.strptime(cadena_hora, "%H:%M")
    if hora.minute == 0:
        return True
    else:
        return False

# Función que revisa que los valores de opción múltiple sean números enteros positivos
def valor_valido(valor):
    try:
        if int(valor) > 0:
            return True
        else:
            return False
    except ValueError:
        return False

# Función que devuelve un objeto 'error' para convertir a formato JSON
def objeto_error(id, title, error, icon, confirm_button):
    objeto = {
        'id': '#{}'.format(id),
        'title': title,
        'error': error,
        'icon': icon,
        'confirmButton': confirm_button
    }
    return objeto

# Función que devuelve un objeto 'success' para convertir a formato JSON
def objeto_success(title, success, icon, confirm_button):
    objeto = {
        'title': title,
        'success': success,
        'icon': icon,
        'confirmButton': confirm_button
    }
    return objeto