# Generated by Django 2.2.5 on 2019-10-03 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_blogs_img2'),
    ]

    operations = [
        migrations.AddField(
            model_name='coment',
            name='noticia',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='cmm', to='blogs.Blogs'),
        ),
    ]