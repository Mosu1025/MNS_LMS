

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_auto_20200730_0746"),
    ]

    operations = [
        migrations.AlterField(
            model_name="semester",
            name="semester",
            field=models.CharField(
                blank=True,
                choices=[("First", "First"), ("Second", "Second"), ("Third", "Third")],
                max_length=10,
            ),
        ),
    ]
