# Generated by Django 4.0.5 on 2022-10-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_alter_payment_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
