# Generated by Django 4.2.4 on 2023-08-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Authentication", "0006_user_role"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="id",
        ),
        migrations.AlterField(
            model_name="user",
            name="telephone",
            field=models.CharField(
                blank=True,
                default="",
                max_length=20,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
