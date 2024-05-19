from django.urls import path
from . import views


urlpatterns = [
    # cars
    path('', views.ListCars.as_view(), name='dashboard'),
    path('car/<int:pk>/', views.CarsDetail.as_view(), name='CarDetail'),
    path('car/add/', views.AddCar.as_view(), name='add_car'),
    path('car/edit/<int:pk>/', views.EditCar.as_view(), name='edit_car'),
    path('car/delete/<int:pk>/', views.DeleteCar.as_view(), name='delete_car'),

    # comments
    path('car/add/comment/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
    path('car/update/comment/<int:pk>/', views.EditComment.as_view(), name='edit_comment'),
    path('car/delete/comment/<int:pk>/', views.DeleteComment.as_view(), name='delete_comment'),

    # profile
    path('my_profile/<int:pk>/', views.MyProfile.as_view(), name='MyProfile'),
    path('my_profile/update/<int:pk>/', views.edit_profile, name='my_profile_update')

]
