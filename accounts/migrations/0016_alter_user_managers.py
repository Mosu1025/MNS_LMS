

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
    ]
