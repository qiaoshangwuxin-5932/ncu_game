import json as simplejson
from Gamer.models import User,Questions
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.shortcuts import HttpResponse
# 分数
@csrf_exempt
def pushScore(request):
    if request.method == 'POST':
        req = simplejson.loads(request.body)
        username = req['username']
        question = req['question']
        answer = req['answer']
        groups = req['groups']
        score = User.objects.filter(username=username).values('score')
        complete = Questions.objects.filter(groups=groups, question=question).values('scorelevel__%s'%(answer))
        for a in complete:
            a = a['scorelevel__%s'%(answer)]
            print(a)
            for score in score:
                score = score['score']
                if complete:
                    a = str(a)
                    User.objects.filter(username=username).update(score=F('score')+a)
                    return HttpResponse('dwad')