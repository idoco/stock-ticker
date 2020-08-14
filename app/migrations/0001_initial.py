# Generated by Django 3.0.8 on 2020-08-14 15:57

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_at', models.DateTimeField(null=True)),
                ('is_disabled', models.BooleanField(default=False)),
                ('python_model', models.CharField(max_length=1024)),
                ('python_arguments', jsonfield.fields.JSONField()),
                ('python_kwargs', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_ticker', models.CharField(max_length=128)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('current_price', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('sold_price', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('purchase_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('sold_at', models.DateTimeField(null=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Portfolio')),
            ],
        ),
        migrations.AddField(
            model_name='portfolio',
            name='algo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Strategy'),
        ),
    ]
