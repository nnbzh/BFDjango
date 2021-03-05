# Generated by Django 3.1.7 on 2021-03-05 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateField()),
                ('due_on', models.DateField()),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('mark', models.BooleanField()),
                ('todos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='main.todos')),
            ],
        ),
    ]
