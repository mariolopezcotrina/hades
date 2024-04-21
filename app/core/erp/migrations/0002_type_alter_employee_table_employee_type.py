# Generated by Django 5.0.4 on 2024-04-21 01:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelTable(
            name='employee',
            table=None,
        ),
        migrations.AddField(
            model_name='employee',
            name='type',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='erp.type'),
        ),
    ]