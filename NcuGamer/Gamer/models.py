from django.db import models
from django.utils.timezone import now
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20,null=False,blank=False,verbose_name='用户名字')
    score = models.IntegerField(null=True,verbose_name='分数') #后端计算的分数，与前段无关
    time = models.DateTimeField(default=now,verbose_name='时间')
    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

class Questions(models.Model):
    choice = (
        ('ADM', '行政组'),
        ('RDC','研发组'),
        ('PRT','产品组'),
        ('DES','设计组'),
        ('OPE','运营组'),
    )
    group = models.CharField(max_length=3,choices=choice,verbose_name='组类')#用来判断题库
    question = models.TextField(verbose_name='问题')
    option1 = models.CharField(max_length=40,verbose_name='选项A')
    option2 = models.CharField(max_length=40,verbose_name='选项B')
    option3 = models.CharField(max_length=40,verbose_name='选项C')
    class Meta:
        db_table = 'question'
        verbose_name='游戏问题'
        verbose_name_plural = verbose_name


class ScoreLevel(models.Model):
    answer = models.ForeignKey(Questions,on_delete=models.SET)
    A = models.IntegerField(verbose_name='20')
    B = models.IntegerField(verbose_name='15')
    C = models.IntegerField(verbose_name='10')
    class Meta:
        db_table = 'level'
        verbose_name = '等级'
        verbose_name_plural = verbose_name

































