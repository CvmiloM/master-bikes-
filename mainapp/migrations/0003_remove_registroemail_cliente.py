# Generated by Django 5.0.6 on 2024-07-15 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_registroemail_usuarioadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registroemail',
            name='cliente',
        ),
    ]
