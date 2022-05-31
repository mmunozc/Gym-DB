# Generated by Django 3.2.8 on 2021-11-03 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sabado'), ('domingo', 'Domingo')], max_length=255)),
                ('hora_inicial', models.TimeField()),
                ('hora_final', models.TimeField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo_muscular', models.CharField(choices=[('pecho', 'Pecho'), ('hombro', 'Hombro'), ('triceps', 'Triceps'), ('biceps', 'Biceps'), ('espalda', 'Espalda'), ('trapecio', 'Trapecio'), ('abdomen', 'Abdomen'), ('isquiotibiales', 'Isquiotibiales'), ('cuadriceps', 'Cuadriceps'), ('gluteos', 'Gluteos')], max_length=255)),
                ('cantidad_ejercicios', models.IntegerField()),
                ('dificultad', models.CharField(choices=[('inicial', 'Inicial'), ('intermedio', 'Intermedio'), ('Avanzado', 'Avanzado')], max_length=255)),
                ('repeticiones', models.IntegerField()),
                ('lista_equipos', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piso', models.CharField(choices=[('primero', 'Primero'), ('segundo', 'Segundo'), ('tercero', 'Tercero'), ('cuarto', 'Cuarto')], max_length=255)),
                ('tipo', models.CharField(choices=[('musculacion', 'Musculacion'), ('cardio', 'Cardio')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('entrenador', 'Entrenador'), ('cliente', 'Cliente'), ('mantenimiento', 'Mantenimiento'), ('servicios varios', 'Servicios varios'), ('recepcion', 'Recepcion')], max_length=255)),
                ('sexo', models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], max_length=255)),
                ('plan', models.CharField(choices=[('dia', 'Dia'), ('mes', 'Mes'), ('trimestral', 'Trimestral'), ('semestral', 'Semestral'), ('anual', 'Anual')], max_length=255)),
                ('remuneracion', models.IntegerField(default=0)),
                ('registro_de_clase', models.ManyToManyField(blank=True, to='gym.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='EquipoDeEntrenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('grupo_muscular', models.CharField(choices=[('pecho', 'Pecho'), ('hombro', 'Hombro'), ('triceps', 'Triceps'), ('biceps', 'Biceps'), ('espalda', 'Espalda'), ('trapecio', 'Trapecio'), ('abdomen', 'Abdomen'), ('isquiotibiales', 'Isquiotibiales'), ('cuadriceps', 'Cuadriceps'), ('gluteos', 'Gluteos')], max_length=255)),
                ('fecha_mantemiento', models.DateField()),
                ('fecha_adquisicion', models.DateField()),
                ('marca', models.CharField(max_length=255)),
                ('cantidad', models.IntegerField()),
                ('zona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym.zona')),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('yoga', 'Yoga'), ('fuerza', 'Fuerza'), ('cardio', 'Cardio'), ('danza', 'Danza'), ('zumba', 'Zumba')], max_length=255)),
                ('costo', models.IntegerField(default=0)),
                ('maximo_personas', models.IntegerField()),
                ('calendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.calendario')),
                ('equipos_de_entrenamiento', models.ManyToManyField(blank=True, to='gym.EquipoDeEntrenamiento')),
                ('rutina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.rutina')),
                ('zona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym.zona')),
            ],
        ),
    ]