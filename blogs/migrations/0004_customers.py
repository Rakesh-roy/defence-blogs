# Generated by Django 3.1.3 on 2020-11-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogsmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('querry', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]
