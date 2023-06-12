# 사용자 브라우저로 응답을 하기 위한 라이브러리 불러들이기
from django.http import HttpResponse
# 템플릿을 불러오는 라이브러리
from django.shortcuts import render
    
def index(request):
    return render(request,		
                  "projectapp/index.html", 
                  {})

def board(request):
    return render(request,		
                  "projectapp/board.html", 
                  {})

def post(request):
    return render(request,		
                  "projectapp/post.html", 
                  {})

def disease(request):
    return render(request,		
                  "projectapp/disease.html", 
                  {})

def disease_result(request):
    return render(request,		
                  "projectapp/disease_result.html", 
                  {})

def mypage(request):
    return render(request,		
                  "projectapp/mypage.html", 
                  {})

def update_mypage(request):
    return render(request,		
                  "projectapp/update_mypage.html", 
                  {})