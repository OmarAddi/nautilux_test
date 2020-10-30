
from views import IntervViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', IntervViewSet)
urlpatterns = router.urls