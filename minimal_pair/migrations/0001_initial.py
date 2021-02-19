# Generated by Django 3.1.1 on 2021-02-11 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ipa_board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinimalPairCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('associated_phoneme', models.ForeignKey(db_column='associated_phoneme', help_text='Associated phoneme', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_phoneme_id', to='ipa_board.phonemeinformation', verbose_name='Associated phoneme')),
                ('phoneme', models.ForeignKey(db_column='phoneme', help_text='Phoneme', on_delete=django.db.models.deletion.CASCADE, related_name='first_phoneme_id', to='ipa_board.phonemeinformation', verbose_name='First phoneme')),
                ('sub_phoneme_type_id', models.ForeignKey(db_column='sub_phoneme_type_id', help_text='Associated phoneme type', on_delete=django.db.models.deletion.CASCADE, to='ipa_board.subphonemetype')),
            ],
            options={
                'db_table': 'minimal_pair_category',
            },
        ),
        migrations.CreateModel(
            name='MinimalPairInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(db_column='label', help_text='Sound name', max_length=254, verbose_name='Sound name')),
                ('ipa_label', models.CharField(db_column='ipa_label', help_text='IPA sound name', max_length=254, verbose_name='IPA sound name')),
                ('associated_sound_id', models.ForeignKey(db_column='associated_sound_id', help_text='Associated sound', on_delete=django.db.models.deletion.CASCADE, to='minimal_pair.minimalpairinformation')),
                ('category_id', models.ForeignKey(db_column='category_id', help_text='Category of the minimal pair sound', on_delete=django.db.models.deletion.CASCADE, to='minimal_pair.minimalpaircategory')),
            ],
            options={
                'db_table': 'minimal_pair_information',
            },
        ),
        migrations.CreateModel(
            name='MinimalPairWordPhonemePlace',
            fields=[
                ('minimal_pair_id', models.OneToOneField(db_column='minimal_pair_id', help_text='Associated minimal pair', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='minimal_pair.minimalpairinformation')),
                ('letters', models.CharField(db_column='letters', help_text='Phoneme letters', max_length=254, null=True, verbose_name='Phoneme letters')),
                ('ipa_letters', models.CharField(db_column='ipa_letters', help_text='IPA phoneme letters', max_length=254, null=True, verbose_name='IPA phoneme letters')),
            ],
            options={
                'db_table': 'minimal_pair_word_phoneme_place',
            },
        ),
    ]