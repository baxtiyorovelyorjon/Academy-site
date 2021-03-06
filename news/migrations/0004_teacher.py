# Generated by Django 4.0.5 on 2022-06-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Media/teach_img')),
                ('teaching_course', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
