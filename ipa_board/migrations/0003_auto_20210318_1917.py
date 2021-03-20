# Generated by Django 3.1.7 on 2021-03-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipa_board', '0002_auto_20210309_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonemeinformation',
            name='sound_file_name',
        ),
        migrations.AddField(
            model_name='phonemeinformation',
            name='sound_file_path',
            field=models.CharField(db_column='sound_file_path', default='a', help_text='Associated file name', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exampleword',
            name='ipa_label',
            field=models.CharField(db_column='ipa_label', default='a', help_text='IPA word label', max_length=254, verbose_name='IPA word label'),
            preserve_default=False,
        ),
    ]