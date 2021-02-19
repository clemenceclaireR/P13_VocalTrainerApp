# Generated by Django 3.1.1 on 2021-02-11 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('minimal_pair', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, db_column='score', null=True)),
                ('date', models.DateTimeField(auto_now_add=True, db_column='date', null=True)),
                ('minimal_pair_category_id', models.ForeignKey(db_column='minimal_pair_category_id', help_text='Score associated category', on_delete=django.db.models.deletion.CASCADE, to='minimal_pair.minimalpaircategory', verbose_name='Score associated category')),
                ('user_id', models.ForeignKey(db_column='user_id', help_text='User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'score',
            },
        ),
    ]