# Generated by Django 5.0.6 on 2024-06-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app101', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='food.jpg', upload_to='images/'),
        ),
    ]
