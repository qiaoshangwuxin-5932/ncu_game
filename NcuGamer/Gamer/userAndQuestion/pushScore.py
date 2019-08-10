import json as simplejson
from Gamer.models import User,Questions
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.http import JsonResponse
from .mad import mad
# 分数
@csrf_exempt
def pushScore(request):
    if request.method == 'POST':
        req = simplejson.loads(request.body.decode('utf-8'))
        username = req['username']
        question = req['question']
        question_id = req['question_id']
        answer = req['answer']
        groups = req['groups']
        question_id = int(question_id)
        list = ['one','two','three','four','five']
        b = list[question_id-1]
        lastAnswer = User.objects.filter(username=username).values('%s'%(b))
        score = User.objects.filter(username=username).values('score')
        complete = Questions.objects.filter(groups=groups, question=question).values('scorelevel__%s'%(answer))
        for a in complete:
            a = a['scorelevel__%s'%(answer)]
            for score in score:
                score = score['score']
                for last in lastAnswer:
                    lastAnswer = last['%s' % (b)]
                    if complete:
                        a = str(a)
                        if lastAnswer is None:
                            User.objects.filter(username=username).update(score=F('score')+a)
                            mad(b, username, answer, groups)
                            if b == 'three':
                                score = User.objects.filter(username=username, score__lte=50)
                                if score:
                                    return JsonResponse(
                                        {
                                            "status": 1,
                                            "success": True,
                                            "spark": True
                                        }
                                    )
                            else:
                                return JsonResponse(
                                    {
                                        "status":1,
                                        "success":True,
                                        "spark":False
                                    }
                                )
                        else:
                            seqs = Questions.objects.filter(groups=groups, question=question).values('scorelevel__%s' % (lastAnswer))
                            for seq in seqs:
                                seq = seq['scorelevel__%s'%(lastAnswer)]
                                seq = str(seq)
                                User.objects.filter(username=username).update(score=F('score') + a)
                                User.objects.filter(username=username).update(score=F('score') - seq)
                                mad(b, username, answer, groups)
                                return JsonResponse(
                                    {
                                        "status": 1,
                                        "success": True,
                                        "message":"修改成功",
                                        "spark":False
                                    }
                                )


