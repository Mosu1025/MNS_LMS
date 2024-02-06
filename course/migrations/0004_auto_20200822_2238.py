

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20200803_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('Bachloar', 'Bachloar Degree'), ('Master', 'Master Degree')], max_length=25, null=True),
        ),
    ]
