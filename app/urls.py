from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('round',views.round, name='round'),
    path('booking',views.booking, name='booking'),
    path('login',views.login,name='login'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('login_data',views.login_data,name='login_data'),
    path('booking_details',views.booking_details, name='booking_details'),
    path('Delete/<int:pk>/',views.Delete, name='Delete'),
    # path('pending_user_count',views.pending_user_count, name='pending_user_count'),
    path('approve_booking/<int:pk>/', views.approve_booking, name='approve_booking'),
    path('round_booking',views.round_booking, name='round_booking'),
    path('roundtrip',views.roundtrip, name='roundtrip'),
    path('approve_round/<int:pk>/',views.approve_round, name='approve_round'),
    path('Delete_round/<int:pk>/',views.Delete_round,name='Delete_round'),
    path('about',views.about, name='about'),

]