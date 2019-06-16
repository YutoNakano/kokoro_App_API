from rest_framework import routers
from .views import QuestionViewSet, ResultViewSet

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'results', ResultViewSet)