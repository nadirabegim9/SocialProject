# Generated by Django 5.0.6 on 2024-06-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='caption_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='caption_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='caption_ru',
            field=models.TextField(null=True),
        ),
    ]