# Generated by Django 4.1.5 on 2023-01-24 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, default=1.0, max_digits=3)),
                ('type', models.CharField(choices=[('addition', 'Addition'), ('division', 'Division'), ('multiplication', 'Multiplication'), ('random_string', 'Random String'), ('square_root', 'Square Root'), ('subtraction', 'Subtraction')], max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=10.0, max_digits=8)),
                ('password', models.CharField(max_length=256)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=1)),
                ('username', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=1.0, max_digits=3)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('operation_response', models.CharField(max_length=256)),
                ('user_balance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('operation_id', models.ForeignKey(db_column='operation_id', on_delete=django.db.models.deletion.PROTECT, to='api.operation')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.PROTECT, to='api.user')),
            ],
        ),
    ]
