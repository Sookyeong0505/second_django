from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render

monthly_challenges = {
    "january": "1월은 새해. 떡국을 먹자!",
    "febuary": "2월은 아직 겨울. 곧 봄이 온다.",
    "march": "3월이다. 봄이 왔다네~. 꽃샘추위 조심!",
    "april": "꽃 피는 4월. 산책을 가야지.",
    "may": "봄봄봄 봄이 왔어요~ 5월이 되었다!",
    "june": "6월에는 사랑하는 이들과 피크닉을 가자.",
    "july": "장미가 만발하는 7월이에요~",
    "august": "으악! 태풍이다!! 8월만 넘기면 가을이야",
    "september": "9월이네. 아직은 덥지만 이제 좀 선선한걸? 곧 단풍이 지겠어.",
    "october": "알록달록한 단풍을 구경하자~ 맛있는 과일이 많은 10월이야",
    "november": "춥다 추워!! 11월은 따뜻하게 집에 있어야지.",
    "december": None
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
    # return HttpResponse(list_items)
    return render(request, "challenges/index.html", {
        "months": months,

    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    # path("<month>", views.monthly_challenges) 맞춰서 작성해야 함
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        return Http404()

