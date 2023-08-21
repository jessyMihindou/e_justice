# Generated by Django 4.2.4 on 2023-08-19 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Authentication", "0003_alter_user_managers"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="lieu_de_naissance",
            field=models.CharField(
                choices=[("etranger", "Étranger"), ("gabon", "Gabon")],
                default="",
                max_length=20,
            ),
        ),
    ]
