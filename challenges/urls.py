from django.urls import path

from . import views

urlpatterns = [
    # 동적 경로 생성
    path("", views.index),  # /challenge/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]