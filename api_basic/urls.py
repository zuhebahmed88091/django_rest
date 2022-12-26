from django.urls import path
from .views import article_list, ArticleAPIView, ArticleDetailsView

urlpatterns = [
    # path("article/", article_list),
    path("article/", ArticleAPIView.as_view()),
    # path("detail/<int:pk>/", article_detail),
    path("detail/<int:id>/", ArticleDetailsView.as_view()),
]