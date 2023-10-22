from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(primary_key = True, max_length = 30, verbose_name = 'Nombre de usuario')
    hashed_salted_password = models.CharField(max_length = 128, verbose_name = 'Contraseña')
    email = models.EmailField(max_length = 254, unique = True)
    phone_number = models.CharField(max_length = 12, unique = True)

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        db_table = 'usuarios'
        ordering = ['username']
    
class Nacionalidad(models.Model):
    cod_nacionalidad = models.CharField(primary_key = True, max_length = 1, verbose_name = 'código de la nacionalidad')
    descripcion_nacionalidad = models.CharField(max_length = 10, verbose_name = 'descripción de la nacionalidad')

    def __str__(self):
        return self.cod_nacionalidad

    class Meta:
        verbose_name = 'nacionalidad'
        verbose_name_plural = 'nacionalidades'
        db_table = 'nacionalidad'
        ordering = ['-cod_nacionalidad']

class Sexo(models.Model):
    cod_sexo = models.AutoField(primary_key = True, verbose_name = 'código del sexo')
    descripcion_sexo = models.CharField(max_length = 10, verbose_name = 'descripción del sexo')

    def __str__(self):
        return self.descripcion_sexo

    class Meta:
        verbose_name = 'sexo'
        verbose_name_plural = 'sexos'
        db_table = 'sexo'
        ordering = ['cod_sexo']

class NecesidadEspecial(models.Model):
    cod_necesidad_especial = models.AutoField(primary_key = True, verbose_name = 'código de la necesidad especial')
    descripcion_necesidad_especial = models.CharField(max_length = 40, verbose_name = 'descripción de la necesidad especial')

    def __str__(self):
        return self.descripcion_necesidad_especial

    class Meta:
        verbose_name = 'necesidad especial'
        verbose_name_plural = 'necesidades especiales'
        db_table = 'necesidad_especial'
        ordering = ['cod_necesidad_especial']

class Especialidad(models.Model):
    cod_especialidad = models.AutoField(primary_key = True, verbose_name = 'código de la especialidad')
    descripcion_especialidad = models.CharField(max_length = 40, verbose_name = 'descripción de la especialidad')

    def __str__(self):
        return self.descripcion_especialidad

    class Meta:
        verbose_name = 'especialidad'
        verbose_name_plural = 'especialidades'
        db_table = 'especialidad'
        ordering = ['cod_especialidad']

class Cliente(models.Model):
    ci_cliente = models.IntegerField(primary_key = True, verbose_name = 'cédula')
    nacionalidad = models.ForeignKey(Nacionalidad, null=True, on_delete = models.SET_NULL, db_column = 'nacionalidad', verbose_name = 'nacionalidad')
    nombres = models.CharField(max_length = 64, verbose_name = 'nombres')
    apellidos = models.CharField(max_length = 64, verbose_name = 'apellidos')
    fecha_nacimiento = models.DateField(verbose_name = 'fecha de nacimiento')
    sexo = models.ForeignKey(Sexo, null = True, on_delete = models.SET_NULL, db_column = 'sexo', verbose_name = 'sexo')
    direccion = models.CharField(max_length = 128, null = True, blank = True, verbose_name = 'dirección')
    necesidad_especial = models.ForeignKey(NecesidadEspecial, null = True, on_delete = models.SET_NULL, db_column = 'necesidad_especial', verbose_name = 'necesidad especial')

    def __str__(self):
        return str(self.ci_cliente)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        db_table = 'clientes'
        ordering = ['ci_cliente']

class Doctor(models.Model):
    ci_doctor = models.IntegerField(primary_key = True, verbose_name = 'cédula')
    nacionalidad = models.ForeignKey(Nacionalidad, null=True, on_delete = models.SET_NULL, db_column = 'nacionalidad', verbose_name = 'nacionalidad')
    nombres = models.CharField(max_length = 64, verbose_name = 'nombres')
    apellidos = models.CharField(max_length = 64, verbose_name = 'apellidos')
    fecha_nacimiento = models.DateField(verbose_name = 'fecha de nacimiento')
    sexo = models.ForeignKey(Sexo, null = True, on_delete = models.SET_NULL, db_column = 'sexo', verbose_name = 'sexo')
    direccion = models.CharField(max_length = 128, null = True, blank = True, verbose_name = 'dirección')
    especialidad = models.ForeignKey(Especialidad, null = True, on_delete = models.SET_NULL, db_column = 'especialidad', verbose_name = 'especialidad')

    def __str__(self):
        cedula = self.ci_doctor
        primer_nombre = self.nombres.split(" ")[0]
        primer_apellido = self.apellidos.split(" ")[0]
        sexo = self.sexo.descripcion_sexo
        if sexo == 'Femenino':
            titulo = 'Dra.'
        else:
            titulo = 'Dr.'
        cadena_doctor = '{0} - {1} {2} {3}'.format(cedula, titulo, primer_nombre, primer_apellido)
        return cadena_doctor

    class Meta:
        verbose_name = 'doctor'
        verbose_name_plural = 'doctores'
        db_table = 'doctores'
        ordering = ['ci_doctor']

class MotivoDeConsulta(models.Model):
    cod_motivo = models.AutoField(primary_key = True, verbose_name = 'código del motivo de consulta')
    descripcion_motivo = models.CharField(max_length = 35, verbose_name = 'descripción del motivo de consulta')

    def __str__(self):
        return self.descripcion_motivo
    
    class Meta:
        verbose_name = 'motivo de consulta'
        verbose_name_plural = 'motivos de consulta'
        db_table = 'motivo_de_consulta'
        ordering = ['cod_motivo']

class Sintoma(models.Model):
    cod_sintoma = models.AutoField(primary_key = True, verbose_name = 'código del síntoma')
    descripcion_sintoma = models.CharField(max_length = 60, verbose_name = 'descripción del síntoma')

    def __str__(self):
        return self.descripcion_sintoma

    class Meta:
        verbose_name = 'síntoma'
        verbose_name_plural = 'síntomas'
        db_table = 'sintoma'
        ordering = ['cod_sintoma']

class Urgencia(models.Model):
    cod_urgencia = models.AutoField(primary_key = True, verbose_name = 'código de la urgencia')
    descripcion_urgencia = models.CharField(max_length = 10, verbose_name = 'descripción de la urgencia')

    def __str__(self):
        return self.descripcion_urgencia

    class Meta:
        verbose_name = 'urgencia'
        verbose_name_plural = 'urgencias'
        db_table = 'urgencia'
        ordering = ['cod_urgencia']

class Cita(models.Model):
    id_cita = models.AutoField(primary_key = True, verbose_name = 'ID de la cita')
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, db_column = 'cliente', verbose_name = 'cliente')
    fecha = models.DateField(verbose_name = 'fecha de la cita')
    hora = models.TimeField(verbose_name = 'hora de la cita')
    motivo = models.ForeignKey(MotivoDeConsulta, null = True, on_delete = models.SET_NULL, db_column = 'motivo', verbose_name = 'motivo de la consulta')
    doctor_cita = models.ForeignKey(Doctor, null = True, default = None, on_delete = models.SET_NULL, db_column = 'doctor_cita', verbose_name = 'doctor solicitado')
    urgencia = models.ForeignKey(Urgencia, null = True, on_delete = models.SET_NULL, db_column = 'urgencia', verbose_name = 'urgencia de la cita')
    detalles = models.CharField(max_length = 256, null = True, blank = True, verbose_name = 'detalles')
    cita_aceptada = models.BooleanField(null = True, blank = True, default = None, verbose_name = 'cita aceptada')

    def __str__(self):
        nombre_cliente = self.cliente.nombres.split(" ", 1)[0]
        apellido_cliente = self.cliente.apellidos.split(" ", 1)[0]
        cliente = nombre_cliente + " " + apellido_cliente
        fecha = self.fecha.strftime("%d-%m-%Y")
        hora = self.hora.strftime("%I:%M %p")
        cita = str(self.cliente) + ". " + cliente + ", " + fecha + " " + hora
        return cita

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['fecha', 'hora'], name='fecha y hora únicas'
            )
        ]
        verbose_name = 'cita'
        verbose_name_plural = 'citas'
        db_table = 'citas'
        ordering = ['fecha', 'hora']
  
class SintomasCita(models.Model):
    id_sintoma_cita = models.AutoField(primary_key = True, verbose_name = 'ID del síntoma de la cita')
    cita = models.ForeignKey(Cita, on_delete = models.CASCADE, db_column = 'cita', verbose_name = 'cita')
    sintoma = models.ForeignKey(Sintoma, null = True, on_delete = models.SET_NULL, db_column = 'sintoma', verbose_name = 'síntoma de la cita')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cita', 'sintoma'], name='síntoma de una cita'
            )
        ]
        verbose_name = 'síntoma de una cita'
        verbose_name_plural = 'síntomas de una cita'
        db_table = 'sintomas_cita'
        ordering = ['cita', 'sintoma']

class Diagnostico(models.Model):
    cod_diagnostico = models.AutoField(primary_key = True, verbose_name = 'código del diagnóstico')
    descripcion_diagnostico = models.CharField(max_length = 40, verbose_name = 'descripción del diagnóstico')

    def __str__(self):
        return self.descripcion_diagnostico

    class Meta:
        verbose_name = 'diagnóstico'
        verbose_name_plural = 'diagnósticos'
        db_table = 'diagnostico'
        ordering = ['cod_diagnostico']

class MotivoDeAusencia(models.Model):
    cod_ausencia = models.AutoField(primary_key = True, verbose_name = 'código del motivo de ausencia')
    descripcion_ausencia = models.CharField(max_length = 40, verbose_name = 'descripción del motivo de ausencia')

    def __str__(self):
        return self.descripcion_ausencia

    class Meta:
        verbose_name = 'motivo de ausencia'
        verbose_name_plural = 'motivos de ausencia'
        db_table = 'motivo_de_ausencia'
        ordering = ['cod_ausencia']

class CitaAceptada(models.Model):
    cita = models.OneToOneField(Cita, primary_key = True, on_delete = models.CASCADE, db_column = 'cita', verbose_name = 'cita')
    doctor = models.ForeignKey(Doctor, null = True, blank = True, default = None, on_delete = models.SET_NULL, db_column = 'doctor', verbose_name = 'cédula del doctor')
    diagnostico = models.ForeignKey(Diagnostico, null = True,  blank = True, default = None, on_delete = models.SET_NULL, db_column = 'diagnostico', verbose_name = 'diagnóstico del paciente')
    cita_cumplida = models.BooleanField(null = True, blank = True, default = None, verbose_name = 'cita cumplida')
    ausencia = models.ForeignKey(MotivoDeAusencia, null = True, blank = True, default = None, on_delete = models.SET_NULL, db_column = 'ausencia', verbose_name = 'motivo de la ausencia')

    class Meta:
        verbose_name = 'cita aceptada'
        verbose_name_plural = 'citas aceptadas'
        db_table = 'citas_aceptadas'
        ordering = ['cita']

class CitaRechazada(models.Model):
    cita = models.OneToOneField(Cita, primary_key = True, on_delete = models.CASCADE, db_column = 'cita', verbose_name = 'cita')

    class Meta:
        verbose_name = 'cita rechazada'
        verbose_name_plural = 'citas rechazadas'
        db_table = 'citas_rechazadas'
        ordering = ['cita']

class Area(models.Model):
    cod_area = models.CharField(primary_key = True, max_length = 4, verbose_name = 'código de área')
    descripcion_area = models.CharField(max_length = 15, verbose_name = 'descripción del código de área')

    def __str__(self):
        return self.cod_area

    class Meta:
        verbose_name = 'área'
        verbose_name_plural = 'áreas'
        db_table = 'area'
        ordering = ['cod_area']

class TelefonosClientes(models.Model):
    id_telefono_cliente = models.AutoField(primary_key = True, verbose_name = 'ID del teléfono del cliente')
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, db_column = 'cliente', verbose_name = 'cliente')
    area = models.ForeignKey(Area, null = True, on_delete = models.SET_NULL, db_column = 'area', verbose_name = 'código de área')
    numero_telefonico = models.CharField(max_length = 7, verbose_name = 'número de teléfono')

    def __str__(self):
        return self.area.cod_area + "-" + self.numero_telefonico

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['area', 'numero_telefonico'], name='teléfono de un cliente'
            )
        ]
        verbose_name = 'teléfono de un cliente'
        verbose_name_plural = 'teléfonos de los clientes'
        db_table = 'telefonos_clientes'
        ordering = ['cliente', 'area', 'numero_telefonico']

class TelefonosDoctores(models.Model):
    id_telefono_doctor = models.AutoField(primary_key = True, verbose_name = 'ID del teléfono del doctor')
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, db_column = 'doctor', verbose_name = 'doctor')
    area = models.ForeignKey(Area, null = True, on_delete = models.SET_NULL, db_column = 'area', verbose_name = 'código de área')
    numero_telefonico = models.CharField(max_length = 7, verbose_name = 'número de teléfono')

    def __str__(self):
        return self.area.cod_area + "-" + self.numero_telefonico

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['area', 'numero_telefonico'], name='teléfono de un doctor'
            )
        ]
        verbose_name = 'teléfono de un doctor'
        verbose_name_plural = 'teléfonos de los doctores'
        db_table = 'telefonos_doctores'
        ordering = ['doctor', 'area', 'numero_telefonico']

class Dominio(models.Model):
    cod_dominio = models.AutoField(primary_key = True, verbose_name = 'código del dominio')
    descripcion_dominio = models.CharField(max_length = 67, verbose_name = 'descripción del dominio')

    def __str__(self):
        return self.descripcion_dominio

    class Meta:
        verbose_name = 'dominio'
        verbose_name_plural = 'dominios'
        db_table = 'dominio'
        ordering = ['cod_dominio']

class EmailsClientes(models.Model):
    id_email_cliente = models.AutoField(primary_key = True, verbose_name = 'ID del email del cliente')
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, db_column = 'cliente', verbose_name = 'cliente')
    nombre_email = models.CharField(max_length = 64, verbose_name = 'nombre del email')
    dominio = models.ForeignKey(Dominio, null = True, on_delete = models.SET_NULL, db_column = 'dominio', verbose_name = 'dominio del correo')

    def __str__(self):
        return self.nombre_email + self.dominio.descripcion_dominio

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nombre_email', 'dominio'], name='email de un cliente'
            )
        ]
        verbose_name = 'email de un cliente'
        verbose_name_plural = 'emails de los clientes'
        db_table = 'emails_clientes'
        ordering = ['cliente', 'nombre_email', 'dominio']

class EmailsDoctores(models.Model):
    id_email_doctor = models.AutoField(primary_key = True, verbose_name = 'ID del email del doctor')
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, db_column = 'doctor', verbose_name = 'doctor')
    nombre_email = models.CharField(max_length = 64, verbose_name = 'nombre del email')
    dominio = models.ForeignKey(Dominio, null = True, on_delete = models.SET_NULL, db_column = 'dominio', verbose_name = 'dominio del correo')

    def __str__(self):
        return self.nombre_email + self.dominio.descripcion_dominio

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nombre_email', 'dominio'], name='email de un doctor'
            )
        ]
        verbose_name = 'email de un doctor'
        verbose_name_plural = 'emails de los doctores'
        db_table = 'emails_doctores'
        ordering = ['doctor', 'nombre_email', 'dominio']

class Parentesco(models.Model):
    cod_parentesco = models.AutoField(primary_key = True, verbose_name = 'código del parentesco')
    descripcion_parentesco = models.CharField(max_length = 20, verbose_name = 'descripción del parentesco')

    def __str__(self):
        return self.descripcion_parentesco

    class Meta:
        verbose_name = 'parentesco'
        verbose_name_plural = 'parentescos'
        db_table = 'parentesco'
        ordering = ['cod_parentesco']

class Familiar(models.Model):
    id_familiar = models.AutoField(primary_key = True, verbose_name = 'ID del familiar')
    nuevo_paciente = models.ForeignKey(Cliente, on_delete = models.CASCADE, db_column = 'nuevo_paciente', related_name = 'nuevo_paciente', verbose_name = 'nuevo paciente')
    familiar = models.ForeignKey(Cliente, on_delete = models.CASCADE, db_column = 'familiar', related_name = 'familiar', verbose_name = 'familiar')
    parentesco = models.ForeignKey(Parentesco, null = True, on_delete = models.SET_NULL, db_column = 'parentesco', verbose_name = 'parentesco')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nuevo_paciente', 'familiar'], name='parentesco único'
            )
        ]
        verbose_name = 'familiar'
        verbose_name_plural = 'familiares'
        db_table = 'familiares'
        ordering = ['familiar', 'nuevo_paciente']