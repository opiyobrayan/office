# Generated by Django 3.1.5 on 2022-08-01 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0013_auto_20220801_1523'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Iec',
        ),
        migrations.DeleteModel(
            name='Out',
        ),
    ]
