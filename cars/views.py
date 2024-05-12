from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View


class ListCars(ListView):
    model = models.Cars
    template_name = 'dashboard.html'
    context_object_name = 'cars'


class CarsDetail(DetailView):
    model = models.Cars
    template_name = 'car_detail.html'
    context_object_name = 'car'


class AddCar(CreateView, LoginRequiredMixin):
    model = models.Cars
    template_name = 'add_car.html'
    fields = ('company', 'model', 'milage', 'year_manufactured', 'about', 'price', 'image')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('dashboard')


class EditCar(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = models.Cars
    fields = ('company', 'model', 'milage', 'year_manufactured', 'about', 'price', 'image')
    template_name = "edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class DeleteCar(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = models.Cars
    success_url = reverse_lazy("dashboard")

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user
