# Generated by Django 4.1.7 on 2023-03-07 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Languages', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Languages.language', verbose_name='Language'),
        ),
    ]
