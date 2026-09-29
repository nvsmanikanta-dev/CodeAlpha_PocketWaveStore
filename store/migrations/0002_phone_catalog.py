from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('store', '0001_initial')]
    operations = [
        migrations.AddField(model_name='product', name='brand', field=models.CharField(blank=True, max_length=60)),
        migrations.AddField(model_name='product', name='storage', field=models.CharField(blank=True, max_length=50)),
        migrations.AddField(model_name='product', name='display', field=models.CharField(blank=True, max_length=60)),
        migrations.AddField(model_name='product', name='battery', field=models.CharField(blank=True, max_length=60)),
        migrations.AddField(model_name='product', name='image_asset', field=models.CharField(blank=True, default='img/products/phone-generic.svg', max_length=120)),
    ]
