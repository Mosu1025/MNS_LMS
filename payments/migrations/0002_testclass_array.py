

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testclass',
            name='array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, null=True, size=200),
        ),
    ]
