

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_delete_testclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
