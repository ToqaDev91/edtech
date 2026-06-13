from edtech.users.urls import urlpatterns as user_urlpatterns
from edtech.enrollment.urls import urlpatterns as enrollment_urlpatterns

app_name = "api"
urlpatterns =user_urlpatterns + enrollment_urlpatterns
