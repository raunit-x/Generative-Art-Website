# Generated by Django 3.1.2 on 2020-10-30 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_sold'),
    ]

    operations = [
        migrations.CreateModel(
            name='AIProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('information', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='static/images')),
            ],
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='printstyle',
            field=models.CharField(choices=[('Canvas', 'Canvas'), ('Matte Paper', 'Matte Paper')], default='Canvas', max_length=25),
        ),
        migrations.CreateModel(
            name='AIProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('artwork_associated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.aiproduct')),
            ],
        ),
    ]
