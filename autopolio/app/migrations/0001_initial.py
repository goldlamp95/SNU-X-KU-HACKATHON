

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
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('upload_file', models.FileField(upload_to='documents/%Y/%m/%d/')),
                ('category', models.CharField(blank=True, default='paper', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('upload_file', models.FileField(null=True, upload_to='documents/%Y/%m/%d/')),
                ('category', models.CharField(blank=True, default='other', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('score', models.IntegerField(blank=True, default=0)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_achieved', models.DateField()),
                ('upload_file', models.FileField(upload_to='documents/%Y/%m/%d/')),
                ('category', models.CharField(blank=True, default='license', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='license', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('upload_file', models.FileField(null=True, upload_to='documents/%Y/%m/%d/')),
                ('category', models.CharField(blank=True, default='intern', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intern', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('summary', models.TextField()),
                ('upload_file', models.FileField(null=True, upload_to='documents/%Y/%m/%d/')),
                ('category', models.CharField(blank=True, default='club', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AutoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('date', models.DateField(null=True)),
                ('high_school', models.CharField(blank=True, default='고등학교를 입력하세요', max_length=30, null=True)),
                ('university', models.CharField(blank=True, default='대학교를 입력하세요', max_length=30, null=True)),
                ('class_year', models.IntegerField(null=True)),
                ('major', models.TextField(null=True)),
                ('profile', models.FileField(null=True, upload_to='documents/%Y/%m/%d/')),
                ('occupation', models.TextField(null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]