# Generated by Django 2.0.6 on 2018-07-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userlogininfo_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogininfo',
            name='action',
            field=models.PositiveSmallIntegerField(choices=[(1, '登录'), (2, '注销')], default=1, verbose_name='动作'),
        ),
    ]
