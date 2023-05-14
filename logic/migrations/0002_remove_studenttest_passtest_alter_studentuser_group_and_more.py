# Generated by Django 4.2.1 on 2023-05-13 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studenttest',
            name='passTest',
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='logic.group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studenttest',
            name='passTest',
            field=models.ManyToManyField(to='logic.test'),
        ),
    ]
