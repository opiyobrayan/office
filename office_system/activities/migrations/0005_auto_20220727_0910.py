# Generated by Django 3.1.5 on 2022-07-27 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20220727_0841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='descriprion',
            new_name='description',
        ),
    ]
