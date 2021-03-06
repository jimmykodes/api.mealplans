# Generated by Django 2.2.7 on 2019-11-17 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_plans', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='grocery_list', to='mealplan.MealPlan')),
            ],
        ),
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('checked', models.BooleanField(default=False)),
                ('grocery_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='mealplan.GroceryList')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('dine in', 'Dine In'), ('dine out', 'Dine Out')], max_length=10)),
                ('link', models.URLField(blank=True, null=True)),
                ('restaurant', models.CharField(blank=True, max_length=256, null=True)),
                ('meal', models.CharField(blank=True, max_length=256, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('meal_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='mealplan.MealPlan')),
            ],
        ),
    ]
