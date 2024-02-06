

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_auto_20200822_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takencourse',
            name='grade',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D', 'D'), ('F', 'F'), ('NG', 'NG')], max_length=2),
        ),
    ]
