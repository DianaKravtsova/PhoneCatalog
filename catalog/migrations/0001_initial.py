# Generated by Django 3.0.3 on 2020-03-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('RegDate', models.DateTimeField(auto_now_add=True)),
                ('Addres', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=30)),
            ],
        ),
    ]
