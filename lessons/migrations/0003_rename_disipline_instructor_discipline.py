# Generated by Django 4.2.5 on 2023-09-17 22:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lessons", "0002_instructor_picture_alter_instructor_facebook_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="instructor",
            old_name="disipline",
            new_name="discipline",
        ),
    ]
