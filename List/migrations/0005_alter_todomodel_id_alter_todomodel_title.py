# Generated by Django 4.2.3 on 2023-12-30 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0004_alter_todomodel_description_alter_todomodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
