# Generated by Django 3.2.7 on 2021-09-22 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu', verbose_name='Menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.menuitem', verbose_name='Parent Item')),
            ],
            options={
                'verbose_name': 'Menu item',
                'verbose_name_plural': 'Menu items',
                'ordering': ('order',),
            },
        ),
    ]
