# Generated by Django 2.2.3 on 2019-08-01 07:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('ADM', '行政组'), ('RDC', '研发组'), ('PRT', '产品组'), ('DES', '设计组'), ('OPE', '运营组')], max_length=3, verbose_name='组类')),
                ('question', models.TextField(verbose_name='问题')),
                ('option1', models.CharField(max_length=40, verbose_name='选项A')),
                ('option2', models.CharField(max_length=40, verbose_name='选项B')),
                ('option3', models.CharField(max_length=40, verbose_name='选项C')),
            ],
            options={
                'verbose_name': '游戏问题',
                'verbose_name_plural': '游戏问题',
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名字')),
                ('score', models.IntegerField(null=True, verbose_name='分数')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='ScoreLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.IntegerField(verbose_name='20')),
                ('B', models.IntegerField(verbose_name='15')),
                ('C', models.IntegerField(verbose_name='10')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.SET, to='Gamer.Questions')),
            ],
            options={
                'verbose_name': '等级',
                'verbose_name_plural': '等级',
                'db_table': 'level',
            },
        ),
    ]