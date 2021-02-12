# Generated by Django 3.1.1 on 2021-02-11 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhonemeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(db_column='type_name', help_text='Type name', max_length=254, verbose_name='Type name')),
            ],
            options={
                'db_table': 'phoneme_type',
            },
        ),
        migrations.CreateModel(
            name='SubPhonemeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtype_name', models.CharField(db_column='subtype_name', help_text='Sub Type name', max_length=254, verbose_name='Sub Type name')),
                ('order', models.IntegerField(db_column='order', help_text='Order in which types are displayed in template', null=True)),
                ('phoneme_type', models.ForeignKey(db_column='phoneme_type_id', help_text='Associated phoneme type', null=True, on_delete=django.db.models.deletion.CASCADE, to='ipa_board.phonemetype')),
            ],
            options={
                'db_table': 'sub_phoneme_type',
            },
        ),
        migrations.CreateModel(
            name='PhonemeInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(db_column='label', help_text='Phoneme name', max_length=254)),
                ('sound_file_name', models.CharField(db_column='sound_file_name', help_text='Associated file name', max_length=254)),
                ('sub_phoneme_type', models.ForeignKey(db_column='sub_phoneme_type_id', help_text='Associated phoneme type', null=True, on_delete=django.db.models.deletion.CASCADE, to='ipa_board.subphonemetype')),
            ],
            options={
                'db_table': 'phoneme_information',
            },
        ),
        migrations.CreateModel(
            name='ExampleWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(db_column='label', help_text='Word name', max_length=254)),
                ('phoneme', models.ForeignKey(db_column='phoneme_id', help_text='Associated phoneme', on_delete=django.db.models.deletion.CASCADE, to='ipa_board.phonemeinformation')),
            ],
            options={
                'db_table': 'example_word',
            },
        ),
    ]
