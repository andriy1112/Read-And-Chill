from django.urls import path, include
from news.views import MyRegisterFormView
from . import views

app_name = 'news'


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',  views.post_detail, name='post_detail'),
    path('accounts/register/', MyRegisterFormView.as_view(), name="register"),
    path('register/', MyRegisterFormView.as_view(), name="register"),
    path('login/', views.PostListView.as_view(), name='post_list'),
]
