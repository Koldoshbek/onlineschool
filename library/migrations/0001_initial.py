# Generated by Django 3.0.3 on 2020-03-06 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('barcode', models.CharField(max_length=12, unique=True)),
                ('writer', models.CharField(max_length=256)),
                ('published', models.DateField(blank=True, null=True)),
                ('creating_date', models.DateField(auto_now_add=True)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Category')),
            ],
        ),
    ]
