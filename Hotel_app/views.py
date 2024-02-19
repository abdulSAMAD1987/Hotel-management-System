from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import HotelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'







class HotelListView(LoginRequiredMixin,ListView):
    model = Hotel
    template_name = 'hotel_list.html'
    context_object_name = 'hotels'
    login_url = 'login'

    def get_queryset(self):
        sort_order = self.request.GET.get('sort', 'newest')
        price_range = self.request.GET.get('price_range')

        hotels = Hotel.objects.all()

        if price_range:
            min_price, max_price = map(int, price_range.split('-'))
            hotels = hotels.filter(price__range=(min_price, max_price))

        if sort_order == 'ascending':
            hotels = hotels.order_by('price')
        elif sort_order == 'descending':
            hotels = hotels.order_by('-price')
        elif sort_order == 'low_to_high':
            hotels = hotels.order_by('price')
        elif sort_order == 'high_to_low':
            hotels = hotels.order_by('-price')
        elif sort_order == 'newest':
            hotels = hotels.order_by('created_at')

        return hotels

class HotelDetailView(LoginRequiredMixin,DetailView):
    model = Hotel
    template_name = 'hotel_detail.html'
    context_object_name = 'hotel'
    login_url = 'login'

class HotelCreateView(LoginRequiredMixin,CreateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'Add_hotel.html'
    success_url = reverse_lazy('hotel_list')
    login_url = 'login'


class HotelUpdateView(LoginRequiredMixin,UpdateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'Add_hotel.html'
    success_url = reverse_lazy('hotel_list')
    login_url = 'login'


class HotelDeleteView(LoginRequiredMixin,DeleteView):
    model = Hotel
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('hotel_list')
    login_url = 'login'


#
# def hotel_list(request):
#     sort_order = request.GET.get('sort', 'newest')
#     price_range = request.GET.get('price_range')
#
#     hotels = Hotel.objects.all()
#
#     if price_range:
#         min_price, max_price = map(int, price_range.split('-'))
#         hotels = hotels.filter(price__range=(min_price, max_price))
#
#     if sort_order == 'ascending':
#         hotels = hotels.order_by('price')
#     elif sort_order == 'descending':
#         hotels = hotels.order_by('-price')
#     elif sort_order == 'low_to_high':
#         hotels = hotels.order_by('price')
#     elif sort_order == 'high_to_low':
#         hotels = hotels.order_by('-price')
#     elif sort_order == 'newest':
#         hotels = hotels.order_by('created_at')
#
#     return render(request, 'hotel_list.html', {'hotels': hotels, 'sort_order': sort_order})
#
#
# # def hotel_list(request):
# #     sort_order = request.GET.get('sort', 'newest')
# #     hotels = Hotel.objects.all()
# #
# #     if sort_order == 'ascending':
# #         hotels = hotels.order_by('price')
# #     elif sort_order == 'descending':
# #         hotels = hotels.order_by('-price')
# #     elif sort_order == 'low_to_high':
# #         hotels = hotels.order_by('price')
# #     elif sort_order == 'high_to_low':
# #         hotels = hotels.order_by('-price')
# #     elif sort_order == 'newest':
# #         hotels = hotels.order_by('created_at')
# #
# #     return render(request, 'hotel_list.html', {'hotels': hotels, 'sort_order': sort_order})
#
#
# def hotel_detail(request, pk):
#     hotel = get_object_or_404(Hotel, pk=pk)
#     return render(request, 'hotel_detail.html', {'hotel': hotel})
#
#
# def hotel_create(request):
#     if request.method == 'POST':
#         form = HotelForm(request.POST, request.FILES)
#         if form.is_valid():
#             hotel = form.save()
#             return redirect('hotel_list')
#     else:
#         form = HotelForm()
#     return render(request, 'Add_hotel.html', {'form': form})
#
#
# def hotel_edit(request, pk):
#     hotel = get_object_or_404(Hotel, pk=pk)
#     if request.method == 'POST':
#         form = HotelForm(request.POST, request.FILES, instance=hotel)
#         if form.is_valid():
#             hotel = form.save()
#             return redirect('hotel_list')
#     else:
#         form = HotelForm(instance=hotel)
#     return render(request, 'Add_hotel.html', {'form': form})
#
#
# def hotel_delete(request, pk):
#     hotel = get_object_or_404(Hotel, pk=pk)
#     hotel.delete()
#     return redirect('hotel_list')
