# Generated by Django 4.0.4 on 2022-05-17 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]