

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200729_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('Bachloar', 'Bachloar Degree'), ('Master', 'Master Degree')], max_length=25, null=True),
        ),
    ]
