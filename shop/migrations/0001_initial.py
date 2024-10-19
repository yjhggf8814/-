# Generated by Django 5.1.1 on 2024-10-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=86)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('price', models.PositiveIntegerField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('stock', models.IntegerField()),
                ('sale', models.PositiveIntegerField()),
            ],
        ),
    ]
