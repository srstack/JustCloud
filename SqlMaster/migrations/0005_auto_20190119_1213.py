# Generated by Django 2.1.5 on 2019-01-19 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SqlMaster', '0004_auto_20181224_2351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='name',
            new_name='user',
        ),
    ]
