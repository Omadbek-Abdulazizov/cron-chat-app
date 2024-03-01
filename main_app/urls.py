from django.urls import path
from .views import HomeView,HodimlarView,ShablonlarView,LavozimlarView,UpdateHodimView,UpdateLavozimView,UpdateShablonView,AddHodimView,AddLavozimView,AddShablonView, LoginView,delete_hodim,delete_lavozim,delete_shablon,logout_view

urlpatterns = [
    path('', HomeView.as_view(), name="home"  ),
    path('hodimlar/', HodimlarView.as_view(), name="hodimlar"),
    path('shablonlar/', ShablonlarView.as_view(), name="shablonlar"),
    path('lavozimlar/', LavozimlarView.as_view(), name="lavozimlar"),
    path('update_hodim/<int:pk>/', UpdateHodimView.as_view(), name="update_hodim"),
    path('update_lavozim/<int:pk>/', UpdateLavozimView.as_view(), name="update_lavozim"),
    path('update_shablon/<int:pk>/', UpdateShablonView.as_view(), name="update_shablon"),
    path('add_hodim/', AddHodimView.as_view(), name="add_hodim"),
    path('add_lavozim/', AddLavozimView.as_view(), name="add_lavozim"),
    path('add_shablon/', AddShablonView.as_view(), name="add_shablon"),
    path('delete_hodim/<int:pk>/', delete_hodim, name="delete_hodim"  ),
    path('delete_lavozim/<int:pk>/', delete_lavozim, name="delete_lavozim"  ),
    path('delete_shablon/<int:pk>/', delete_shablon, name="delete_shablon"  ),
    # path('filter_by_lavozim/<str:data>', filter_by_lavozim, name="filter_by_lavozim"),
    path('login/', LoginView.as_view(), name="login"  ),
    path('logout/', logout_view, name="logout"  ),
]