

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="semester",
            name="semester",
            field=models.CharField(
                blank=True,
                choices=[("First", "First"), ("Second", "Second"), ("Third", "Third")],
                max_length=10,
                unique=True,
            ),
        ),
    ]
