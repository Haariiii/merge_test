# Generated by Django 4.2.2 on 2023-06-19 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videogallery", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gallery",
            name="like_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="gallery", name="user_id", field=models.TextField(default=""),
        ),
    ]