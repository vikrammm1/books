# Generated by Django 3.2.16 on 2023-03-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_shop', '0003_alter_author_year_dead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='year_dead',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
