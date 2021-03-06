# Generated by Django 2.2.24 on 2021-07-15 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default='')),
                ('type', models.CharField(choices=[('Web', 'Web'), ('Mobile', 'Mobile')], max_length=255)),
                ('framework', models.CharField(choices=[('Django', 'Django'), ('React Native', 'React Native')], max_length=255)),
                ('domain_name', models.CharField(default='', max_length=50)),
                ('screenshot', models.ImageField(blank=True, upload_to='screenshots')),
            ],
            options={
                'verbose_name': 'App',
                'verbose_name_plural': 'Apps',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField()),
                ('app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.App')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='home.Plan')),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.AddConstraint(
            model_name='plan',
            constraint=models.CheckConstraint(check=models.Q(price__gte=0), name='plan_price_gte_0'),
        ),
        migrations.AddField(
            model_name='app',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apps', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='app',
            index=models.Index(fields=['name'], name='app_name_idx'),
        ),
        migrations.AddIndex(
            model_name='app',
            index=models.Index(fields=['domain_name'], name='domain_name_idx'),
        ),
        migrations.AddConstraint(
            model_name='app',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='unique_app_name'),
        ),
    ]
