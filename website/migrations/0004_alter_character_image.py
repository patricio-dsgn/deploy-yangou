# Generated by Django 4.0.4 on 2022-05-17 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_character_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(null=True, upload_to='website/characters/'),
        ),
    ]