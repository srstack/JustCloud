# Generated by Django 2.1.5 on 2019-02-10 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SqlMaster', '0012_auto_20190203_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='model',
            field=models.BooleanField(db_index=True, default=0, verbose_name='订阅/推送'),
        ),
        migrations.AlterField(
            model_name='data',
            name='waring',
            field=models.NullBooleanField(db_index=True, default=None, verbose_name='正常/异常'),
        ),
    ]
