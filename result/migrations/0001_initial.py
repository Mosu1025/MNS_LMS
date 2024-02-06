

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("course", "0001_initial"),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TakenCourse",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "assignment",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "mid_exam",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "quiz",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "attendance",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "final_exam",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "total",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "grade",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("A+", "A+"),
                            ("A", "A"),
                            ("A-", "A-"),
                            ("B+", "B+"),
                            ("B", "B"),
                            ("B-", "B-"),
                            ("C+", "C+"),
                            ("C", "C"),
                            ("C-", "C-"),
                            ("D", "D"),
                            ("F", "F"),
                            ("NG", "NG"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "point",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "comment",
                    models.CharField(
                        blank=True,
                        choices=[("PASS", "PASS"), ("FAIL", "FAIL")],
                        max_length=200,
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taken_courses",
                        to="course.Course",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.Student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Result",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gpa", models.FloatField(null=True)),
                ("cgpa", models.FloatField(null=True)),
                (
                    "semester",
                    models.CharField(
                        choices=[
                            ("First", "First"),
                            ("Second", "Second"),
                            ("Third", "Third"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("Level course", "Level course"),
                            ("Bachloar", "Bachloar"),
                            ("Master", "Master"),
                        ],
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.Session",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.Student",
                    ),
                ),
            ],
        ),
    ]
