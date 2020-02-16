from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('add_event/', views.add_event, name='add_event'),
    path('add_work_event/', views.add_work_event, name='add_work_event'),
    path('add_education_event/', views.add_education_event, name='add_education_event'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('profile/', views.ProfileListView.as_view(), name='profile'),
    path('requests/', views.RequesterListView.as_view(), name='requests'),
    path('requests/<int:pk>/verify_event', views.verify_event, name='verify_event'),
    path('share_with/', views.ShareWithView.as_view(), name='share_with'),
    path('doc_share_with/', views.DocumentView.as_view(), name='doc_share_with'),
    path('share_with/<int:pk>/share', views.share, name='share'),
    path('doc_share_with/<int:pk>/doc_share', views.document_share, name='doc_share'),
    path('review/', views.ReviewListView.as_view(), name='review'),
    path('actions/', views.ActionsListView.as_view(), name='actions'),
    path('upload/', views.upload, name='upload'),
]
