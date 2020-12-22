"""Diploma URL Configuration

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
from cinema.views import SignInView, SignOutView, SignUpView, main_page, TodaySessionsList, TomorrowSessionsList, \
    MoviesList

urlpatterns = [
    path('', main_page, name='main_page'),
    path('admin/', admin.site.urls),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('todayfilms/', TodaySessionsList.as_view(), name='today_schedule'),
    path('tomorrowfilms/', TomorrowSessionsList.as_view(), name='tomorrow_schedule'),
    path('list-of-movies/', MoviesList.as_view(), name='list-of-movies'),
    # path('my_tickets', )

]
