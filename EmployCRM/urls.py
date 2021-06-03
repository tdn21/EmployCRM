from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from students.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name="login"),
    path('students/', include('students.urls', namespace="students")),
    path('colleges/', include('colleges.urls', namespace="colleges")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('links/', include('links.urls', namespace="links")),
    path('admin-signup/', SignupView.as_view(), name="signup"),
    path('logout/', LogoutView.as_view(), name="logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
