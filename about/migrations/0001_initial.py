# Generated by Django 4.1.7 on 2023-04-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='about/')),
                ('from_adress', models.CharField(max_length=100)),
                ('lives_in', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]