# Generated by Django 3.2.4 on 2021-06-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210616_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_name',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
