#from django.conf.urls import url

from rest_framework.routers import DefaultRouter
from .api import ListApi, CardApi


#urlpatterns = [
 #   url(r'^lists$', ListApi.as_view()),
  #  url(r'^cards$', CardApi.as_view())

#]

router = DefaultRouter()
router.register(r'lists', ListApi)
router.register(r'cards', CardApi)

urlpatterns = router.urls
