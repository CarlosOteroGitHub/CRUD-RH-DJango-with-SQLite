# Generated by Django 3.2.8 on 2021-10-25 21:09

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.IntegerField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('nacimiento', models.DateField()),
                ('descripcion', models.TextField(max_length=100)),
            ],
        ),
    ]
