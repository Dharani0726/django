# Generated by Django 3.0.4 on 2020-05-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tsignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
            ],
        ),
    ]
