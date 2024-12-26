from django.urls import path

from . import views

urlpatterns = [
    # 동적 경로 생성
    path("", views.index, name="index"),  # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]