# Generated by Django 3.2.8 on 2021-10-12 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstrava', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='likes',
        ),
        migrations.AlterField(
            model_name='record',
            name='sport_type',
            field=models.CharField(choices=[('jogging', 'JOGGING'), ('pull-ups', 'PULL-UPS'), ('push-ups', 'PUSH-UPS'), ('crunches', 'CRUNCHES'), ('squats', 'SQUATS')], default='jogging', max_length=10),
        ),
    ]