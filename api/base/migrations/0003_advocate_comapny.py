# Generated by Django 4.2.4 on 2023-12-20 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='comapny',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.company'),
        ),
    ]