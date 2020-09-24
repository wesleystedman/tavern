from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.landing, name="landing"),
    path('groups/', views.groups_index, name="groups_index"),
    path('groups/<int:group_id>/', views.groups_detail, name='groups_detail'),
    path('groups/<int:pk>/contenders/', views.contender_detail, name='contender_detail'),
    path('groups/create/', views.GroupCreate.as_view(), name='groups_create'),
    path('groups/<int:pk>/delete/', views.GroupDelete.as_view(), name='group_delete'),
    path('groups/<int:pk>/update/', views.GroupUpdate.as_view(), name='group_update'),				
    path('accounts/signup/', views.signup, name='signup'),
    path('lfg/', views.lfg, name='lfg'),
    path('lfg/add-contender/', views.add_contender, name='add_contender'),
    path('profiles/create/', views.ProfileCreate.as_view(), name='profile_form'),
    path('profiles/', views.profile, name='profile'),
    path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
]

