# Generated by Django 3.1.2 on 2020-10-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cNAME', models.CharField(max_length=20)),
                ('cID', models.CharField(max_length=20)),
                ('cGENDER', models.CharField(max_length=10)),
                ('cAGE', models.CharField(blank=True, default='', max_length=10)),
                ('cWHERE', models.CharField(max_length=100)),
                ('cPAINSITE', models.CharField(max_length=100)),
                ('cWHEN', models.CharField(max_length=100)),
                ('cHOW', models.CharField(max_length=100)),
                ('cPROVOCATION', models.CharField(blank=True, default='', max_length=100)),
                ('cPAINLEVEL', models.CharField(max_length=100)),
                ('cPI', models.CharField(max_length=500)),
            ],
        ),
    ]
