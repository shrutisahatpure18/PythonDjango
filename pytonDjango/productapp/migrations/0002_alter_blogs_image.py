# Generated by Django 5.0.4 on 2024-04-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(upload_to='productapp/static/blogs'),
        ),
    ]
