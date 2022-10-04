from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("data", models.ImageField(upload_to="")),
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Pereval",
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
                ("beauty_title", models.CharField(default="пер.", max_length=10)),
                ("title", models.CharField(max_length=25)),
                ("other_titles", models.CharField(max_length=25)),
                ("connect", models.CharField(blank=True, max_length=25)),
                ("add_time", models.DateTimeField(auto_now_add=True)),
                ("level_winter", models.CharField(blank=True, max_length=2)),
                ("level_summer", models.CharField(blank=True, max_length=2)),
                ("level_autumn", models.CharField(blank=True, max_length=2)),
                ("level_spring", models.CharField(blank=True, max_length=2)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("RJ", "модерация не пройдена"),
                            ("PD", "принято на модерацию"),
                            ("NW", "новый"),
                            ("AC", "модерация прошла успешно"),
                        ],
                        default="NW",
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("fam", models.CharField(max_length=25)),
                ("name", models.CharField(max_length=15)),
                ("otc", models.CharField(max_length=15)),
                ("phone", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="PerevalImage",
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
                (
                    "foto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="pereval.image",
                    ),
                ),
                (
                    "pereval",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pereval.pereval",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Coords",
            fields=[
                (
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("data", models.ImageField(upload_to="")),
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Pereval",
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
                ("beauty_title", models.CharField(default="пер.", max_length=10)),
                ("title", models.CharField(max_length=25)),
                ("other_titles", models.CharField(max_length=25)),
                ("connect", models.CharField(blank=True, max_length=25)),
                ("add_time", models.DateTimeField(auto_now_add=True)),
                ("level_winter", models.CharField(blank=True, max_length=2)),
                ("level_summer", models.CharField(blank=True, max_length=2)),
                ("level_autumn", models.CharField(blank=True, max_length=2)),
                ("level_spring", models.CharField(blank=True, max_length=2)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("RJ", "модерация не пройдена"),
                            ("PD", "принято на модерацию"),
                            ("NW", "новый"),
                            ("AC", "модерация прошла успешно"),
                        ],
                        default="NW",
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("fam", models.CharField(max_length=25)),
                ("name", models.CharField(max_length=15)),
                ("otc", models.CharField(max_length=15)),
                ("phone", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="PerevalImage",
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
                (
                    "foto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="pereval.image",
                    ),
                ),
                (
                    "pereval",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pereval.pereval",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Coords",
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
                ("latitude", models.CharField(max_length=15)),
                ("longitude", models.CharField(max_length=15)),
                ("height", models.CharField(max_length=15)),
                (
                    "pereval",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pereval.pereval",
                    ),
                ),
            ],
        ),
    ]