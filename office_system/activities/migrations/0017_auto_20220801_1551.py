# Generated by Django 3.1.5 on 2022-08-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0016_delete_iec'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Out',
            new_name='Out_Author',
        ),
        migrations.AlterField(
            model_name='store',
            name='date',
            field=models.DateField(max_length=60, verbose_name='Date'),
        ),
    ]
