# Generated by Django 3.2.3 on 2021-07-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='notas',
        ),
        migrations.AddField(
            model_name='autor',
            name='notas',
            field=models.TextField(blank=True),
        ),
    ]
