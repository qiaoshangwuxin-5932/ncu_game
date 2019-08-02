from django.shortcuts import render
'''
# Create your sql here.
from django.shortcuts import render, HttpResponse, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
import os
from django.core.serializers import serialize
from ..models import User,Questions
import json as simplejson

def update(request):
    # 研发
    # 1  ABC
    group = '研发组'
    question = '程序员们的头发数量可能截然不同，但说的话却常相似。研发最喜欢说的一句话可能是？'
    option1 = '我好菜啊'
    option2 = '我这里没问题呀'
    option3 = '还可以加需求'
    Questions.objects.create(group=group,question=question,option1=option1,option2=option2,option3=option3)
    # 2 BCA
    group = '研发组'
    question = '一天，某前端和后端正在讨论用户注册问题，你发现，前端把____和____数据传给后端就能够最好实现用户注册。'
    option1 = 'username  email'
    option2 = 'email  password'
    option3 = 'username  password'
    Questions.objects.create(group=group,question=question,option1=option1,option2=option2,option3=option3)
    # 3 ABC 
    group = '研发组'
    question = '研发测试产品注册功能时，发现某用户登陆使用了未经注册的用户名，于是后端该向前端发送____反映此情况？'
    option1 = 'unknown user'
    option2 = 'u u'
    option3 = '404'
    Questions.objects.create(group=group,question=question,option1=option1,option2=option2,option3=option3)
    # 4 CAB
    group = '研发组'
    question = '要知道程序员的双肩包里，可能会有一切。以下最不可能出现在程序员双肩包里的是？'
    option1 = '折叠板凳'
    option2 = '电脑'
    option3 = 'ipad'
    Questions.objects.create(group=group,question=question,option1=option1,option2=option2,option3=option3)
    # 5 CBA 
    group = '研发组'
    question = '某产品上线前，前后端开始了紧张的接口调试，此时后端给出的数据结构混乱，如果你是前端，你会_____'
    option1 = '把后端扔出去'
    option2 = '自己沉住气自己解析'
    option3 = '让后端优化结构数据'
    Questions.objects.create(group=group,question=question,option1=option1,option2=option2,option3=option3)
    #产品
    # 1 BAC 
    group = '产品组'
    question = '产品们都有着共同的酸甜苦辣，产品最喜欢说的一句话可能是？'
    option1 = '实现这个不难的'
    option2 = '给个排期吧'
    option3 = '这个功能要不砍了吧？'
    Questions.objects.create(group=group,question=question,option1=option1,option2=option2,option3=option3)
    # 2 CAB
    group = '产品组'
    question = '你突然想到了关于新产品的绝妙想法，你该用什么方式清楚地向研发表述你的idea？'
    option1 = '给他你的手绘原型图'
    option2 = '用你的高超口才叙述'
    option3 = '用AXURE出好原型图'
    Questions.objects.create(group=group,question=question,option1=option1,option2=option2,option3=option3)
    # 3 BAC 
    group = '产品组'
    question = '一个成熟的产品，和研发在新产品上有了矛盾时，很有可能采取什么手段？'
    option1 = '扮演舔狗'
    option2 = '激情辩论'
    option3 = '冷处理'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 4 CBA 
    group = '产品组'
    question = '以下哪项不是产品需要做的事？'
    option1 = '需求分析'
    option2 = '用户调研、'
    option3 = 'UI设计'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 5 CAB 
    group = '产品组'
    question = '你认为一个起步阶段的产品经理最需要看？'
    option1 = '通识读本'
    option2 = '摄影画册'
    option3 = '专业入门书籍'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 设计
    #   1 ABC
    group = '设计组'
    question = '一个设计最喜欢说的话可能是？'
    option1 = '改哪里啊？'
    option2 = '再过几天给你'
    option3 = '我尽快把下一版给你'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 2 ABC
    group = '设计组'
    question = '下面哪项是设计最常使用的软件？'
    option1 = 'PS'
    option2 = 'AI'
    option3 = 'MS Office'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 3 CAB
    group = '设计组'
    question = '作为迎新视频的筹划，现在有三个预选摄影师，各有其优势，综合考量一番后，你敲定_____作为本次大会御用摄影'
    option1 = '手不抖，但只会相机自动模式'
    option2 = '手易抖，有多年单反使用经验'
    option3 = '设备佳，手抖，只会自动模式'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 4 ABC 
    group = '设计组'
    question = '设计在听到什么需求时，容易流泪？'
    option1 = '把它设计成五彩斑斓的黑'
    option2 = '这个logo占的面积小一点，整体大一点'
    option3 = '把标题排成竖排文字叭，再换个字体'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 5 ABC 
    group = '设计组'
    question = '以下哪项很有可能属于UI设计的错误？'
    option1 = '控件不统一'
    option2 = '缺少层级差异'
    option3 = '页面部分留白'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 运营组
    # 1 ABC 
    group = '运营组'
    question = '运营组最喜欢说的话可能是？'
    option1 = '这个热点必须追！'
    option2 = '怎么和用户说明情况啊？'
    option3 = '我不关心热点，我只关心你'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 2 ACB 
    group = '运营组'
    question = '今天你在QQ平台值班，需要发一条说说。这时，有三个内容集体撞车，你要选择：'
    option1 = '某单车为南大出了高颜值定制款'
    option2 = '世界5G技术又取得新进展'
    option3 = '四六级考试报名链接正式发布'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 3 ACB 
    group = '运营组'
    question = '写推送是运营的必修课，在确定以某热点为主题后，你为封面头图愁秃了头，这张图要怎么办呢？'
    option1 = 'P图达人本人，自己做 '
    option2 = '虽然平时都用美图秀秀，但还是试试看 '
    option3 = '找设计组寻求帮助'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 4 ABC 
    group = '运营组'
    question = '运营的选题脑洞，有时候大到不可思议，你认为一个运营的选题最有可能来自？'
    option1 = '学校闲逛途中'
    option2 = '刷微博追剧'
    option3 = '选题会上'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 5 CAB 
    group = '运营组'
    question = '运营不仅需要单纯的内容输出，还需要冷静地分析数据。以下各项最可能不是运营关心的数据是？'
    option1 = '发出内容推送的一小时阅读量'
    option2 = '推送或活动达到的转化率'
    option3 = '一篇推送完成所需的总时长'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    #行政
    # 1 CBA 
    group = '行政组'
    question = '家园的行政几乎是十八般技能槽统统点满的存在，以下各项行政可能不会的是？'
    option1 = 'Ms Office'
    option2 = 'PR'
    option3 = 'Vue'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 2 CBA 
    group = '行政组'
    question = '温暖如行政，再细心记下工作室每个小伙伴的生日后，还会精心准备祝福语，最近运营的学姐要过生日了，下面哪句祝福语最合适呢？'
    option1 = '前辈，祝您生日快乐！'
    option2 = 'xxx终于20岁啦，你已经是个成熟的女大学生了，生日快乐！'
    option3 = '祝为家园倾注能量的美丽运营生日快乐！你是最棒的话题制造者，推送都能10w + ~'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 3 BCA 
    group = '行政组'
    question = '家园每年的全体大会都令人期待，本次由你筹备。为了征集节目，你要怎么推动身边的家园er们参与节目呢？'
    option1 = '在线征集，筒子们自愿报名~'
    option2 = '暗中观察，说服潜在表演嘉宾'
    option3 = '靠自己，嗨不嗨就靠你了靠自己，嗨不嗨就靠你了'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 4 BCA 
    group = '行政组'
    question = '收集了几十名程序员的无课情况之后，你需要做一张无课统计的电统计表。怎么才能让这张表格尽可能美观呢？'
    option1 = '设置表格固定的行高列宽'
    option2 = '表格完成后转为PDF格式'
    option3 = '表格的行列空间尽可能拉大'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    # 5 ABC 
    group = '行政组'
    question = '行政不是带来惊喜，就是在带来惊喜的路上。圣诞节时你要策划一个活动，以下哪项可能是次优先级的考虑因素？'
    option1 = '活动参与人数'
    option2 = '活动大致预算'
    option3 = '活动流程内容'
    Questions.objects.create(group=group, question=question, option1=option1, option2=option2, option3=option3)
    return HttpResponse('MMM')
'''