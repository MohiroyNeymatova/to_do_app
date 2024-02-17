# Generated by Django 4.1.6 on 2023-09-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'active'), (2, 'finished')], default=1)),
            ],
        ),
    ]
