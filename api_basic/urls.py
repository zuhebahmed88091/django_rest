from django.urls import path, include
from .views import article_list, ArticleAPIView, ArticleDetailsView, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # path("article/", article_list),
    path("viewset/", include(router.urls)),
    path("viewset/<int:pk>", include(router.urls)),
    path("article/", ArticleAPIView.as_view()),
    # path("detail/<int:pk>/", article_detail),
    path("detail/<int:id>/", ArticleDetailsView.as_view()),
    path("generic/article/<int:id>/", GenericAPIView.as_view()),
]