# Generated by Django 5.0.6 on 2024-05-31 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("WhatIsHumanDesign", "0007_yourauth_yourenergy_yourroad_yourrole"),
    ]

    operations = [
        migrations.CreateModel(
            name="HumanFather",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300, verbose_name="內容標題")),
                ("content", models.TextField(verbose_name="標題內容")),
                ("imgs_url", models.URLField(blank=True, verbose_name="內容圖片")),
                (
                    "layout_key",
                    models.ForeignKey(
                        default="人類圖是你的人生使用說明書",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WhatIsHumanDesign.layoutwhat",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ra Uru Hu = 引進人類圖(索引值8)",
                "verbose_name_plural": "Ra Uru Hu = 引進人類圖(索引值8)",
            },
        ),
        migrations.CreateModel(
            name="YourMin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300, verbose_name="內容標題")),
                ("content", models.TextField(verbose_name="標題內容")),
                ("imgs_url", models.URLField(blank=True, verbose_name="內容圖片")),
                (
                    "layout_key",
                    models.ForeignKey(
                        default="人類圖是你的人生使用說明書",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WhatIsHumanDesign.layoutwhat",
                    ),
                ),
            ],
            options={
                "verbose_name": "輪迴交叉 = 你的命運(索引值7)",
                "verbose_name_plural": "輪迴交叉 = 你的命運(索引值7)",
            },
        ),
    ]
