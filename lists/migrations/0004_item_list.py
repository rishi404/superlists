# Generated by Django 2.0.7 on 2018-08-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, on_delete=None, to='lists.List'),
        ),
    ]
