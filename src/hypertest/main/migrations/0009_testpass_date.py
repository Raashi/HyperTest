# Generated by Django 3.0.4 on 2020-04-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200406_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='testpass',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Pass date'),
        ),
    ]
