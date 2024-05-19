from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import AddCommentForm, EditCommentForm, EditProfileForm


# cars
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


# comments
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


class EditComment(LoginRequiredMixin, UpdateView):
    def get(self, request, pk):
        comment = models.Comments.objects.get(pk=pk)
        edit_comment_form = EditCommentForm(instance=comment)
        context = {
            'comment': comment,
            'edit_comment_form': edit_comment_form
        }
        return render(request, 'edit_comment.html', context=context)

    def post(self, request, pk):
        comment = models.Comments.objects.get(pk=pk)
        edit_comment_form = EditCommentForm(request.POST, instance=comment)
        if edit_comment_form.is_valid():
            edit_comment_form = edit_comment_form.save(commit=False)
            edit_comment_form.car_id = comment.car_id
            edit_comment_form.save()
            return redirect('CarDetail', pk=comment.car_id)
        else:
            context = {
                'edit_comment_form': edit_comment_form
            }
            print('======================> form invalid <=======================')
            return render(request, 'edit_comment.html', context=context)


class DeleteComment(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = models.Comments
    success_url = reverse_lazy("dashboard")
    template_name = 'confirm_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


# profile
class MyProfile(View):
    def get(self, request, pk):
        my_profile = models.Accounts.objects.get(pk=pk)
        context = {
            'my_profile': my_profile
        }
        return render(request, 'profile.html', context=context)


class EditProfile(UpdateView):
    model = models.Accounts
    template_name = 'profile_update.html'
    fields = ('password', 'username', 'bio', 'age', 'profile_picture')

    success_url = reverse_lazy('dashboard')