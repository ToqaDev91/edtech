from django.urls import path
from .views import test_api, start_enrollment

urlpatterns = [
    path('enrollment/test/', test_api, name='test-enrollment'),
    path('enrollment/start/', start_enrollment, name='start-enrollment'),
]