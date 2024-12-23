from django.urls import path

from . import views

urlpatterns = [
    # 동적 경로 생성
    path("<month>", views.monthly_challenges)
]