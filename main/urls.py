from .views import (
    user_login, 
    user_dashboard, 
    delete_paper, 
    profile,
    achievements,
    remove_publication,
    remove_conference,
    remove_patent,
    time_table,
    logout_user
)
from django.urls import path


urlpatterns = [
    path('', user_login, name='login'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('delete_paper/', delete_paper, name='delete_paper'),
    path('profile/', profile, name='profile'),
    path('achievements/', achievements, name='achievements'),
    path('pub_del/', remove_publication, name='remove_publication'),
    path('con_del/', remove_conference, name='remove_conference'),
    path('pat_del/', remove_patent, name='remove_patent'),
    path('time_table/', time_table, name='time_table'),
    path('logout/', logout_user, name='logout'),
]