# Generated by Django 2.2.5 on 2019-09-27 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogs_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='img',
            field=models.CharField(max_length=500),
        ),
    ]
