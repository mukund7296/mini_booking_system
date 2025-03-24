from django.urls import path
from . import views

urlpatterns = [
    path('', views.FacilityListView.as_view(), name='facility_list'),
    path('book/', views.BookingCreateView.as_view(), name='booking_create'),
    path('my-bookings/', views.BookingListView.as_view(), name='booking_list'),
    path('register/', views.register, name='register'),  # Add this line

]
