# Generated by Django 3.2 on 2021-04-27 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('percelorder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=200, null=True)),
                ('district', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='percel',
            name='name',
        ),
        migrations.AddField(
            model_name='percel',
            name='cod_charge',
            field=models.FloatField(default=0, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='percel',
            name='delivery_charge',
            field=models.FloatField(default=0, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='percel',
            name='return_charge',
            field=models.FloatField(default=0, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='percel',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='percelorder.address'),
        ),
    ]
