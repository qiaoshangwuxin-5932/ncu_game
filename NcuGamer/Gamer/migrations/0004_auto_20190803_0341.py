# Generated by Django 2.2.3 on 2019-08-03 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gamer', '0003_auto_20190803_0322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='group',
            new_name='groups',
        ),
    ]
