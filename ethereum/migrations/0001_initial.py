# Generated by Django 4.0.5 on 2022-06-20 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ethereum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('domain', models.CharField(max_length=10)),
                ('data', models.TextField(default='{}')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_ethereums', to='category.category')),
            ],
            options={
                'db_table': 'ethereum',
                'ordering': ('-id',),
                'managed': True,
                'unique_together': {('name',)},
            },
        ),
    ]