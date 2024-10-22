# Generated by Django 5.1 on 2024-08-08 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0003_ubicacion_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenaza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenazas', to='mapa.ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Conservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conservaciones', to='mapa.ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habitats', to='mapa.ubicacion')),
            ],
        ),
        migrations.DeleteModel(
            name='AreaProtegida',
        ),
        migrations.DeleteModel(
            name='Especie',
        ),
    ]
