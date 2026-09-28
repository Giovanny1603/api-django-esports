from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EquipeViewSet, JogadorViewSet

router = DefaultRouter()
router.register(r'equipes', EquipeViewSet)
router.register(r'jogadores', JogadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]