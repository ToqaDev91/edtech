from django.urls import path
from .views import start_enrollment, get_count

urlpatterns = [
    path('enrollment/start/', start_enrollment, name='start-enrollment'),
    path('enrollment/count/', get_count, name='count-enrollment')
]