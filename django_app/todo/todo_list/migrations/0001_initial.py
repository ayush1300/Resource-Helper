# Generated by Django 3.2.4 on 2021-06-12 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ComponentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('link', models.CharField(max_length=1000)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_list.list')),
            ],
        ),
    ]