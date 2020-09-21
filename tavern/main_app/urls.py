from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.landing, name="landing"),
    path('groups/', views.groups_index, name="groups_index"),
    path('groups/create/', views.GroupCreate.as_view(), name='groups_create'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profiles/create/', views.BioCreate.as_view(), name='bio'),
    path('lfg/', views.lfg, name='lfg'),
    path('lfg/add-contender/', views.add_contender, name='add_contender'),
]

