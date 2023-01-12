# Generated by Django 4.1.4 on 2023-01-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appss', '0004_alter_userotp_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('email', models.EmailField(default=None, max_length=100)),
                ('message', models.TextField(max_length=1000)),
                ('subject', models.TextField(default=None, max_length=1000)),
                ('from_email', models.EmailField(default=None, max_length=100)),
                ('file', models.FileField(default=None, upload_to='')),
            ],
        ),
    ]