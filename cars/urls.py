from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCars.as_view(), name='dashboard'),
    path('car/<int:pk>/', views.CarsDetail.as_view(), name='CarDetail'),
    path('car/add/', views.AddCar.as_view(), name='add_car'),
    path('car/edit/<int:pk>/', views.EditCar.as_view(), name='edit_car'),
    path('car/delete<int:pk>', views.DeleteCar.as_view(), name='delete_car')
    
]
