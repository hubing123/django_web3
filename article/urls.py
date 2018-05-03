from django.urls import path
from article.views import *

urlpatterns = [
    path('<int:article_id>', article_detail, name="article_detail"),
    path('',articles_list,name="articles_list")

]