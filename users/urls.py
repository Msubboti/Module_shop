from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .views import Registration

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='costom_registration/login.html'), name='login'),
    path('registration/', Registration, name='registration'),
    #path('personal_cabinet/<int:pk>', UserDetailView.as_view(), name='personal_cabinet'),
    #path('Conformation/', ConformationEmail.as_view(), name='conformation_email'),
    path(
        "logout/",
        LogoutView.as_view(template_name='costom_registration/logout.html', next_page=None),
        name="logout",
    ),
]
