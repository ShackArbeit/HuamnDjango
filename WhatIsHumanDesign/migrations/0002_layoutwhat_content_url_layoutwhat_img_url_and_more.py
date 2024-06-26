# Generated by Django 4.1.5 on 2024-05-26 01:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("WhatIsHumanDesign", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="layoutwhat",
            name="content_url",
            field=models.CharField(blank=True, max_length=255, verbose_name="內容連結"),
        ),
        migrations.AddField(
            model_name="layoutwhat",
            name="img_url",
            field=models.URLField(blank=True, max_length=800, verbose_name="圖片連結"),
        ),
        migrations.AlterField(
            model_name="layoutwhat",
            name="content",
            field=models.TextField(max_length=800, verbose_name="小節內容"),
        ),
        migrations.AlterField(
            model_name="layoutwhat",
            name="title",
            field=models.CharField(max_length=255, verbose_name="小節標題"),
        ),
    ]
