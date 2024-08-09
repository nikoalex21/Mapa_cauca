# Generated by Django 4.2 on 2024-08-09 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0007_rename_descripcion_hostales_descripcionhostal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
    ]