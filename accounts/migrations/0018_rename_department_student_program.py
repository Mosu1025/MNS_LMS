

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_departmenthead_options_alter_parent_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='department',
            new_name='program',
        ),
    ]
