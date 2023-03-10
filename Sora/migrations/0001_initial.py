# Generated by Django 4.1.7 on 2023-03-10 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sora',
            fields=[
                ('soraid', models.PositiveSmallIntegerField(primary_key=True, serialize=False, verbose_name='Sora Number')),
                ('name', models.CharField(max_length=15, unique=True, verbose_name='Name')),
                ('native', models.CharField(max_length=15, unique=True, verbose_name='Native')),
                ('place', models.CharField(choices=[('1', 'Makia'), ('2', 'Madania')], max_length=1, verbose_name='Disembarkation Place')),
                ('noOfVerses', models.PositiveSmallIntegerField(null=True, verbose_name='number Of Verses')),
            ],
            options={
                'verbose_name': 'Sora',
                'verbose_name_plural': 'Souar',
            },
        ),
    ]