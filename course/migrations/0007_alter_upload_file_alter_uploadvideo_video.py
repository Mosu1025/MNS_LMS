

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_courseoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(help_text='Valid Files: pdf, docx, doc, xls, xlsx, ppt, pptx, zip, rar, 7zip', upload_to='course_files/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7zip'])]),
        ),
        migrations.AlterField(
            model_name='uploadvideo',
            name='video',
            field=models.FileField(help_text='Valid video formats: mp4, mkv, wmv, 3gp, f4v, avi, mp3', upload_to='course_videos/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'mkv', 'wmv', '3gp', 'f4v', 'avi', 'mp3'])]),
        ),
    ]
