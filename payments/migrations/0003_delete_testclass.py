

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_testclass_array'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestClass',
        ),
    ]
