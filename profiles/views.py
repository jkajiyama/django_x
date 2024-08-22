from django.views.generic import DetailView, UpdateView
from .models import Profile
from . import forms
from django.urls import reverse_lazy


# Create your views here.
class ProfileView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    is_my_profile = False

    def get_queryset(self):
        return super().get_queryset().select_related('user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_my_profile'] = self.is_my_profile
        return context


class MyProfileView(ProfileView):
    is_my_profile = True

    def get_queryset(self):
        self.kwargs.update(pk=self.request.user.pk)
        return super().get_queryset()


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = forms.ProfileUpdateForm
    template_name = 'profiles/update.html'
    success_url = reverse_lazy('profiles:my')

    def get_queryset(self):
        self.kwargs.update(pk=self.request.user.pk)
        return super().get_queryset()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
