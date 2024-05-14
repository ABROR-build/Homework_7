from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import AddCommentForm


class ListCars(ListView):
    model = models.Cars
    template_name = 'dashboard.html'
    context_object_name = 'cars'


class CarsDetail(View):
    def get(self, request, pk):
        car = models.Cars.objects.get(pk=pk)
        comments = models.Comments.objects.filter(car=pk)
        print(comments)
        context = {
            'car': car,
            'comments': comments
        }
        return render(request, 'car_detail.html', context=context)


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
    template_name = 'confirm_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class AddComment(LoginRequiredMixin, View):
    def get(self, request, pk):
        cars = models.Cars.objects.get(pk=pk)
        add_comment_form = AddCommentForm()
        context = {
            'cars': cars,
            'add_comment_form': add_comment_form
        }
        return render(request, 'add_comment.html', context=context)

    def post(self, request, pk):
        cars = models.Cars.objects.get(pk=pk)
        add_comment_form = AddCommentForm(request.POST)
        if add_comment_form.is_valid():
            comment = models.Comments.objects.create(
                comment=add_comment_form.cleaned_data['comment'],
                car=cars,
                user=request.user,
            )

            comment.save()
            return redirect('CarDetail', pk=pk)


class EditComment(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = models.Comments
    fields = ['comment']
    template_name = "edit_comment.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    success_url = reverse_lazy('dashboard')


class DeleteComment(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = models.Comments
    success_url = reverse_lazy("dashboard")
    template_name = 'confirm_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
