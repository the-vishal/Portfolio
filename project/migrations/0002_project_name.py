# Generated by Django 2.2.1 on 2019-06-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
