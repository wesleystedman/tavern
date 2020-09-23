from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.landing, name="landing"),
    path('groups/', views.groups_index, name="groups_index"),
    path('groups/<int:group_id>/', views.groups_detail, name='groups_detail'),
    path('groups/create/', views.GroupCreate.as_view(), name='groups_create'),
    path('accounts/signup/', views.signup, name='signup'),
    path('lfg/', views.lfg, name='lfg'),
    path('lfg/add-contender/', views.add_contender, name='add_contender'),
    path('profiles/create/', views.profile_create, name='profile')
]

