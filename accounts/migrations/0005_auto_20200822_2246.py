

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200822_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/%y/%m/%d/'),
        ),
    ]
