from django.views.generic import View
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login as auth_login

from .forms import UserLoginForm, UserRegisterForm

# Create your views here.


class LoginPageView(View):
    template_name = 'Log/login.html'
    form_class = UserLoginForm
    redirect_authenticated_user=True,
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                auth_login(request, user)
                return redirect(to= reverse_lazy('Quran:Home'))
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


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
