# Generated by Django 4.0.2 on 2022-04-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_remove_usuarios_contrasena'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='contrasena',
            field=models.CharField(default='no_contraseña', max_length=200),
        ),
    ]
