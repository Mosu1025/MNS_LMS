

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20200822_2238'),
        ('accounts', '0010_auto_20210401_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_dep_head',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='DepHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.program')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
