from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Nacionalidad)
class NacionalidadAdmin(admin.ModelAdmin):
    list_display = ('cod_nacionalidad', 'descripcion_nacionalidad')

@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    list_display = ('cod_sexo', 'descripcion_sexo')

@admin.register(NecesidadEspecial)
class NecesidadEspecialAdmin(admin.ModelAdmin):
    list_display = ('cod_necesidad_especial', 'descripcion_necesidad_especial')

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('cod_especialidad', 'descripcion_especialidad')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nacionalidad', 'ci_cliente', 'nombres', 'apellidos', 'fecha_nacimiento', 'sexo', 'necesidad_especial')
    ordering = ('ci_cliente',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('nacionalidad', 'ci_doctor', 'nombres', 'apellidos', 'fecha_nacimiento', 'sexo', 'especialidad')
    ordering = ('ci_doctor',)

@admin.register(MotivoDeConsulta)
class MotivoDeConsultaAdmin(admin.ModelAdmin):
    list_display = ('cod_motivo', 'descripcion_motivo')

@admin.register(Sintoma)
class SintomaAdmin(admin.ModelAdmin):
    list_display = ('cod_sintoma', 'descripcion_sintoma')

@admin.register(Urgencia)
class UrgenciaAdmin(admin.ModelAdmin):
    list_display = ('cod_urgencia', 'descripcion_urgencia')

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id_cita', 'cliente', 'fecha', 'hora', 'motivo', 'urgencia', 'cita_aceptada')

@admin.register(SintomasCita)
class SintomasCitaAdmin(admin.ModelAdmin):
    list_display = ('cita', 'sintoma')

@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('cod_diagnostico', 'descripcion_diagnostico')

@admin.register(MotivoDeAusencia)
class MotivoDeAusenciaAdmin(admin.ModelAdmin):
    list_display = ('cod_ausencia', 'descripcion_ausencia')

@admin.register(CitaAceptada)
class CitaAceptadaAdmin(admin.ModelAdmin):
    list_display = ('cita', 'doctor', 'diagnostico', 'cita_cumplida', 'ausencia')

@admin.register(CitaRechazada)
class CitaRechazadaAdmin(admin.ModelAdmin):
    list_display = ('cita',)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('cod_area', 'descripcion_area')

@admin.register(TelefonosClientes)
class TelefonosClientesAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'area', 'numero_telefonico')

@admin.register(TelefonosDoctores)
class TelefonosDoctoresAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'area', 'numero_telefonico')

@admin.register(Dominio)
class DominioAdmin(admin.ModelAdmin):
    list_display = ('cod_dominio', 'descripcion_dominio')

@admin.register(EmailsClientes)
class EmailsClientesAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'nombre_email', 'dominio')

@admin.register(EmailsDoctores)
class EmailsDoctoresAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'nombre_email', 'dominio')

@admin.register(Parentesco)
class ParentescoAdmin(admin.ModelAdmin):
    list_display = ('cod_parentesco', 'descripcion_parentesco')

@admin.register(Familiar)
class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('nuevo_paciente', 'familiar', 'parentesco')