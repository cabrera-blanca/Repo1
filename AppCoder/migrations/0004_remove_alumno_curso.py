# Generated by Django 5.0.3 on 2024-03-31 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_profesores_delete_profesor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='curso',
        ),
    ]