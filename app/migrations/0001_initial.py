# Generated by Django 4.2.7 on 2024-04-06 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('mr_num', models.IntegerField(primary_key=True, serialize=False)),
                ('pr_num', models.IntegerField()),
                ('po_num', models.CharField(max_length=50)),
            ],
        ),
    ]
