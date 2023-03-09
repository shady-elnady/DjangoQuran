from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView

from .forms import UserRegisterForm

# Create your views here.


class Signup(SuccessMessageMixin, CreateView):
    form = UserRegisterForm
    # fields = [
    #     "username",
    #     "email",
    #     "password1",
    #     "password2",
    # ]
    # model = User
    template_name = 'Log/signup.html'
    success_url = reverse_lazy('Quran:Home')
