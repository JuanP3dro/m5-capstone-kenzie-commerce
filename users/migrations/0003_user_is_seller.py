# Generated by Django 4.2 on 2023-05-02 21:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_delete_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_seller",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]