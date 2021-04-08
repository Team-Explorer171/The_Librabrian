# Generated by Django 3.1.7 on 2021-04-03 12:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('cover', models.ImageField(upload_to='book_cover')),
                ('author', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, max_length=25000, null=True)),
                ('available', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=255, unique=True)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('section', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(max_length=25)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_library.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_library.student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_library.category'),
        ),
    ]