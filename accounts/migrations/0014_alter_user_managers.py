

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0013_alter_departmenthead_id_alter_parent_id_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
    ]
