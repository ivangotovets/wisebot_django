# Generated by Django 4.2.2 on 2023-06-29 13:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_alter_message_options_remove_message_author"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="message",
            options={
                "ordering": ("-pub_date",),
                "verbose_name": "Цитата",
                "verbose_name_plural": "Цитаты",
            },
        ),
    ]