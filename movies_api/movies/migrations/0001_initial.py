# Generated by Django 3.0.7 on 2020-06-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=255)),
                ('poster_path', models.CharField(max_length=100, null=True)),
                ('ranking', models.PositiveSmallIntegerField(default=0)),
                ('director', models.CharField(max_length=100, null=True)),
                ('trailer', models.URLField(null=True)),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]