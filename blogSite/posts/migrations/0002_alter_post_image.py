# Generated by Django 5.1.4 on 2025-01-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
    ]
