# Generated by Django 4.1.4 on 2022-12-12 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0002_especialidad_motivodeconsulta_nacionalidad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sintoma',
            fields=[
                ('cod_sintoma', models.AutoField(primary_key=True, serialize=False, verbose_name='código del síntoma')),
                ('descripcion_sintoma', models.CharField(max_length=60, verbose_name='descripción del síntoma')),
            ],
            options={
                'verbose_name': 'síntoma',
                'verbose_name_plural': 'síntomas',
                'db_table': 'sintoma',
                'ordering': ['cod_sintoma'],
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id_cita', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la cita')),
                ('fecha', models.DateField(verbose_name='fecha de la cita')),
                ('hora', models.TimeField(verbose_name='hora de la cita')),
                ('detalles', models.CharField(blank=True, max_length=256, null=True, verbose_name='detalles')),
                ('cita_aceptada', models.BooleanField(blank=True, default=None, null=True, verbose_name='cita aceptada')),
                ('cliente', models.ForeignKey(db_column='cliente', on_delete=django.db.models.deletion.CASCADE, to='Citas.cliente', verbose_name='cliente')),
                ('motivo', models.ForeignKey(db_column='motivo', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Citas.motivodeconsulta', verbose_name='motivo de la consulta')),
                ('urgencia', models.ForeignKey(db_column='urgencia', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Citas.urgencia', verbose_name='urgencia de la cita')),
            ],
            options={
                'verbose_name': 'cita',
                'verbose_name_plural': 'citas',
                'db_table': 'citas',
                'ordering': ['fecha', 'hora'],
            },
        ),
        migrations.AddConstraint(
            model_name='cita',
            constraint=models.UniqueConstraint(fields=('fecha', 'hora'), name='fecha y hora únicas'),
        ),
    ]
