# Generated by Django 3.0.4 on 2020-04-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_test_passed_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'ordering': ['-id'], 'verbose_name': 'Test', 'verbose_name_plural': 'Tests'},
        ),
        migrations.AddField(
            model_name='test',
            name='publish_date',
            field=models.DateTimeField(null=True, verbose_name='Publish date'),
        ),
    ]
