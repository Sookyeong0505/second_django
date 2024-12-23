from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def monthly_challenges(request, month): # path("<month>", views.monthly_challenges) 맞춰서 작성해야 함
    challenge_text = None
    if month == 'january':
        challenge_text = '1월은 새해. 떡국을 먹자!'
    elif month == 'febuary':
        challenge_text = '"2월은 아직 겨울. 곧 봄이 온다.'
    elif month == "march":
        challenge_text = '3월이다. 봄이 왔다네~.'
    elif month == 'april':
        challenge_text = '꽃 피는 4월. 산책을 가야지.'
    else:
        return HttpResponseNotFound("이 월은 지원되지 않습니다.")
    return HttpResponse(challenge_text)