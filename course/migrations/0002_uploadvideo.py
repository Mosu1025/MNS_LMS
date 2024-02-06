

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('video', models.FileField(upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'mkv', 'wmv', '3gp', 'f4v', 'avi', 'mp3'])])),
                ('summary', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
    ]
