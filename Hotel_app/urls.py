# from django.urls import path
# from .views import *
# #
# urlpatterns = [
#     path('', hotel_list, name='hotel_list'),
#     path('hotel/<int:pk>/', hotel_detail, name='hotel_detail'),
#     path('hotel/new/', hotel_create, name='hotel_create'),
#     path('hotel/<int:pk>/edit/', hotel_edit, name='hotel_edit'),
#     path('hotel/<int:pk>/delete/', hotel_delete, name='hotel_delete'),
#     path('login/',login_view, name='login'),
#     path('signup/',signup ,name='signup'),
#
#
# ]
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', HotelListView.as_view(), name='hotel_list'),
    path('hotels/<int:pk>/', HotelDetailView.as_view(), name='hotel_detail'),
    path('hotels/create/', HotelCreateView.as_view(), name='hotel_create'),
    path('hotels/edit/<int:pk>/', HotelUpdateView.as_view(), name='hotel_edit'),
    path('hotels/delete/<int:pk>/', HotelDeleteView.as_view(), name='hotel_delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

]