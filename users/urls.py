from django.urls import path, re_path
from .views import UserRegisterView, UserEditView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name='register'),
    path("edit_profile/", UserEditView.as_view(), name='edit-profile'),

]
