# Generated by Django 4.0.3 on 2022-04-05 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment_app', '0004_alter_contact_date_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_birth',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
