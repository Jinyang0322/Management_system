# Generated by Django 2.2.2 on 2021-12-07 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysystem', '0002_cornellstu_netid'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu1', models.BooleanField(default=False)),
                ('stu2', models.BooleanField(default=False)),
                ('stu3', models.BooleanField(default=False)),
                ('stu4', models.BooleanField(default=False)),
                ('stu5', models.BooleanField(default=False)),
                ('stu6', models.BooleanField(default=False)),
                ('stu7', models.BooleanField(default=False)),
                ('stu8', models.BooleanField(default=False)),
                ('stu9', models.BooleanField(default=False)),
                ('stu10', models.BooleanField(default=False)),
            ],
        ),
    ]