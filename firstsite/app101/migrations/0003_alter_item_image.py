# Generated by Django 5.0.6 on 2024-06-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app101', '0002_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Fcoming-soon-food&psig=AOvVaw1wT9XH85Gljii9tqyNHDDs&ust=1719154536718000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCOCBrO2774YDFQAAAAAdAAAAABAP', max_length=500),
        ),
    ]
