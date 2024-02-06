

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200730_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='default.png', null=True, upload_to='profile_pictures/%y/%m/%d/'),
        ),
    ]
