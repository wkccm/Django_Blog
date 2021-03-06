# Generated by Django 4.0.4 on 2022-04-20 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
