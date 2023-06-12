from django.urls import path
from . import views		

urlpatterns = [
    # http://127.0.0.1:8000/project/

    # 인덱스 페이지
    path('',views.index),
    path('index/',views.index),
    # 게시판
    path('board/',views.board),
    # 게시글
    path('post/',views.post),
    # 진단하기
    path('disease/',views.disease),
    # 진단 결과
    path('disease_result/',views.disease_result),
    # 마이 페이지
    path('mypage/',views.mypage),
    # 회원 정보 수정
    path('update_mypage/',views.update_mypage),

]
