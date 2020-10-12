# Generated by Django 2.0.1 on 2019-12-21 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('supported', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]