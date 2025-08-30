from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign-up/',views.sign_up,name='sign_up'),
    path('sign-out/',views.sign_out,name='sign_out'),
    path('sign-in/',views.sign_in,name='sign_in'),
    path('view-profile/',views.view_profile,name='view_profile'),
    path('edit-profile/',views.edit_profile,name='edit_profile'),
]