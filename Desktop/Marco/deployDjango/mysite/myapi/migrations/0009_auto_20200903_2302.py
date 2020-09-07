# Generated by Django 2.2 on 2020-09-03 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_auto_20200902_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseTitle', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('year', models.CharField(default=2020, max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='top_skills',
            field=models.ManyToManyField(related_name='company', to='myapi.TopSkills'),
        ),
    ]
