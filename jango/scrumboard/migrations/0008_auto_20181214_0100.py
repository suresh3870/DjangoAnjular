# Generated by Django 2.1.4 on 2018-12-13 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0007_auto_20181214_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='scrumboard.List'),
        ),
    ]
