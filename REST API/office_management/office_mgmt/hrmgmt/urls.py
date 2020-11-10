from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('employee-view', views.EmployeeViewSet,basename='employee-view')
urlpatterns = [
    path('',include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]

#path('', include(router.urls)),