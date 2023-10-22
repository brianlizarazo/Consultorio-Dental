import smtplib
from decouple import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
from babel.dates import format_date

# Función para enviar un correo electrónico de la cuenta de correo electrónico oficial de la Clínica Dental Díaz a un paciente en específico
def enviar_email(destinatario, asunto, para, mensaje):
  fecha = date.today()
  hoy = format_date(fecha, format='full', locale='es_VE').capitalize()
  mime = MIMEMultipart()
  mime['From'] = config('EMAIL_USERNAME')
  mime['To'] = destinatario
  mime['Subject'] = asunto
  formato_html = """
    <h1 style="font-size: 2rem; font-weight: 700; text-align: center;">Clínica Dental Díaz</h1>
    <br>
    <p style="margin-bottom: 1rem"><b>De: </b>Clínica Dental Díaz</p>
    <p><b>Para: </b>{}</p>
    <p><b>Fecha: </b>{}</p>
    <p>{}</p>
    <footer style="text-align: center;">
      <p><b>Clínica Dental Díaz</b></p>
      <p>Avenida Bermúdez, Torre Royal, Piso 3, Oficina 32. Los Teques - Edo. Miranda</p>
      <p>0212-3215062 / 0414-1240945</p>
    </footer>
  """.format(para, hoy, mensaje)

  formato = MIMEText(formato_html, 'html')
  mime.attach(formato)

  # Se crea una conexión con Gmail por medio del protocolo SMTP
  servidor = smtplib.SMTP(config('EMAIL_HOSTNAME'), config('EMAIL_TLS_PORT'))
  # servidor = smtplib.SMTP('localhost')

  # Se pone la conexión SMTP en modo TLS (Transport Layer Security)
  servidor.starttls()

  # Se inicia sesión en un servidor SMTP que requiere autenticación
  servidor.login(config('EMAIL_USERNAME'), config('EMAIL_PASSWORD'))

  try:
    # Se envia el correo electrónico
    servidor.sendmail(config('EMAIL_USERNAME'), destinatario, mime.as_string())
    print('¡El correo electrónico fue enviado exitosamente!')
  except:
    print('No se encontró la dirección de correo electrónico ingresada')

  # Termina la sesión SMTP y cierra la conexión
  servidor.quit()

# Función para enviar un correo electrónico de la cuenta de correo electrónico oficial de la Clínica Dental Díaz a la misma cuenta con un mensaje del paciente
def enviar_mensaje(nombre, apellido, email, phone, mensaje):
  fecha = date.today()
  hoy = format_date(fecha, format='full', locale='es_VE').capitalize()
  mime = MIMEMultipart()
  mime['From'] = config('EMAIL_USERNAME')
  mime['To'] = config('EMAIL_USERNAME')
  mime['Subject'] = 'Comentario desde el sitio web'
  formato_html = """
    <h1 style="font-size: 2rem; font-weight: 700; text-align: center;">Comentario desde el sitio web</h1>
    <br>
    <p style="margin-bottom: 1rem"><b>De: </b>{}</p>
    <p><b>Para: </b>Clínica Dental Díaz</p>
    <p><b>Correo electrónico: </b>{}</p>
    <p><b>Número de teléfono: </b>{}</p>
    <p><b>Fecha: </b>{}</p>
    <p>{}</p>
  """.format(nombre + " " + apellido, email, phone, hoy, mensaje)
  formato = MIMEText(formato_html, 'html')
  mime.attach(formato)

  # Se crea una conexión con Gmail por medio del protocolo SMTP
  servidor = smtplib.SMTP(config('EMAIL_HOSTNAME'), config('EMAIL_TLS_PORT'))
  # servidor = smtplib.SMTP('localhost')

  # Se pone la conexión SMTP en modo TLS (Transport Layer Security)
  servidor.starttls()

  # Se inicia sesión en un servidor SMTP que requiere autenticación
  servidor.login(config('EMAIL_USERNAME'), config('EMAIL_PASSWORD'))

  try:
    # Se envia el correo electrónico
    servidor.sendmail(config('EMAIL_USERNAME'), config('EMAIL_USERNAME'), mime.as_string())
    print('¡El correo electrónico fue enviado exitosamente!')
  except:
    print('No se encontró la dirección de correo electrónico ingresada')

  # Termina la sesión SMTP y cierra la conexión
  servidor.quit()
