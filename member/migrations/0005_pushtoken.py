# Generated by Django 3.2.3 on 2021-07-02 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_member_login_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PushToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat_form', models.CharField(blank=True, choices=[('WEB', 'WEB'), ('IPHONE', 'IPHONE'), ('ANDROID', 'ANDROID')], default='WEB', max_length=10)),
                ('udid', models.CharField(blank=True, max_length=64, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_push_tokens', to='member.member')),
            ],
            options={
                'db_table': 'push_token',
                'ordering': ('-id',),
                'managed': True,
                'unique_together': {('member', 'plat_form')},
            },
        ),
    ]
