# Generated by Django 3.1 on 2020-08-25 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_menu_menugroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='origin_information',
            field=models.TextField(),
        ),
    ]
