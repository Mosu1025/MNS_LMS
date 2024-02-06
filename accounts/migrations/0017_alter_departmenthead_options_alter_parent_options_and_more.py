

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departmenthead',
            options={'ordering': ('-user__date_joined',)},
        ),
        migrations.AlterModelOptions(
            name='parent',
            options={'ordering': ('-user__date_joined',)},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('-student__date_joined',)},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('-date_joined',)},
        ),
    ]
