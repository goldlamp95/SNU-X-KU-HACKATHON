"""autopolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 랜딩 페이지가 로그인에 같이 있음
    path('', views.login, name="login"),
    # 1번
    path('main', views.main, name="main")
    # 2번
    path('create', views.create, name="create"),
    # 3번
    path('resume/<int:user_pk>', views.resume, name="resume"),
    # 4번
    path('detail_license/<int:user_pk>/<int:license_pk>', views.detail_license, name="detail_license"),
    path('detail_intern/<int:user_pk>/<int:intern_pk>', views.detail_intern, name="detail_intern"),
    path('detail_club/<int:user_pk>/<int:club_pk>', views.detail_club, name="detail_club"),
    path('detail_paper/<int:user_pk>/<int:paper_pk>', views.detail_paper, name="detail_paper"),
    path('detail_other/<int:user_pk>/<int:other_pk>', views.detail_other, name="detail_other"),
    # 5번
    path('update_license/<int:user_pk>/<int:license_pk>', views.update_license, name="update_license"),
    path('update_intern/<int:user_pk>/<int:intern_pk>', views.update_intern, name="update_intern"),
    path('update_club/<int:user_pk>/<int:club_pk>', views.update_club, name="update_club"),
    path('update_paper/<int:user_pk>/<int:paper_pk>', views.update_paper, name="update_paper"),
    path('update_other/<int:user_pk>/<int:other_pk>', views.update_other, name="update_other"),
    # 6번
    path('delete_license/<int:user_pk>/<int:license_pk>', views.delete_license, name="delete_license"),
    path('delete_intern/<int:user_pk>/<int:intern_pk>', views.delete_intern, name="delete_intern"),
    path('delete_club/<int:user_pk>/<int:club_pk>', views.delete_club, name="delete_club"),
    path('delete_paper/<int:user_pk>/<int:paper_pk>', views.delete_paper, name="delete_paper"),
    path('delete_other/<int:user_pk>/<int:other_pk>', views.delete_other, name="delete_other"),
    # 7번
    path('lookup', views.lookup, name="lookup"),
    path('blurredlist/<int:user_pk>', views.blurredlist, name="blurredlist"),
    # authentication
    path('registration/signup', views.signup, name="signup"),
    path('registration/logout', views.logout, name="logout"),
]
