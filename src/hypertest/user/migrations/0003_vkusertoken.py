# Generated by Django 3.0.4 on 2020-03-29 19:15

from django.db import migrations, models
import django.db.models.deletion
import hypertest.user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_vkuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='VKUserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, default=hypertest.user.models.generate_vk_user_token, max_length=24, null=True, verbose_name='Token')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='token', to='user.VKUser', verbose_name='VK user')),
            ],
            options={
                'verbose_name': "VK user's token",
                'verbose_name_plural': "VK users' tokens",
                'db_table': 'vk_user_token',
            },
        ),
    ]