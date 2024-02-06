

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_rename_department_student_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]
