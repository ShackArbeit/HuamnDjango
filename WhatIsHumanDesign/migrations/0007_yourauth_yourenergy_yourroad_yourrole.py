# Generated by Django 5.0.6 on 2024-05-30 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("WhatIsHumanDesign", "0006_remove_layoutwhat_content_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="YourAuth",
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
                "verbose_name": "內在權威 = 做決定的方法(索引值4)",
                "verbose_name_plural": "內在權威 = 做決定的方法(索引值4)",
            },
        ),
        migrations.CreateModel(
            name="YourEnergy",
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
                "verbose_name": "能量中心 = 你的強弱(索引值5)",
                "verbose_name_plural": "能量中心 = 你的強弱(索引值5)",
            },
        ),
        migrations.CreateModel(
            name="YourRoad",
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
                "verbose_name": "通道 = 你的天賦(索引值6)",
                "verbose_name_plural": "通道 = 你的天賦(索引值6)",
            },
        ),
        migrations.CreateModel(
            name="YourRole",
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
                "verbose_name": "人生角色(索引值3)",
                "verbose_name_plural": "人生角色(索引值3)",
            },
        ),
    ]