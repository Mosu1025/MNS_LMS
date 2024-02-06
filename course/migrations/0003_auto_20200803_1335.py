

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_uploadvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadvideo',
            name='video',
            field=models.FileField(upload_to='course_videos/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'mkv', 'wmv', '3gp', 'f4v', 'avi', 'mp3'])]),
        ),
    ]
