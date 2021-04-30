# Generated by Django 3.2 on 2021-04-30 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('symbole', models.CharField(max_length=50)),
                ('price', models.FloatField(blank=True, default=0)),
                ('rank', models.IntegerField(blank=True, default=0)),
                ('image', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['rank'],
            },
        ),
    ]
