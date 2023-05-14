# Generated by Django 4.2.1 on 2023-05-13 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0002_remove_studenttest_passtest_alter_studentuser_group_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studenttest',
            name='passTest',
        ),
        migrations.AddField(
            model_name='studenttest',
            name='passTest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='logic.test'),
        ),
    ]