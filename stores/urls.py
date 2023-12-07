from django.urls import path
from . import views

urlpatterns = [
    path('',views.PizzeriaListAPIView.as_view(), name="pizzeria_list"),
    path('<int:id>/',views.PizzerialRetrieveAPIView.as_view(), name="pizzeria_detail"),
    path('create/', views.PizzeriaCreateAPIView.as_view(), name='pizzeria_create'),
    path('update/<int:id>/',views.PizzeriaRetriveUpdate.as_view(), name="pizzeria_update")
]