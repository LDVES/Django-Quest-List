from django.shortcuts import render,  redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView
from user_auth_app.forms import UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import logout

# Create your views here.
class UserLogin(FormView):
    template_name = 'user_auth_app/forms/user_login_form.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('quests_manager:index')

    #Checking if user is logged
    def get(self, request):
       if request.user.is_authenticated:
           return redirect('quests_manager:index')
       else:
           return render(request, self.template_name, { 'form' : self.form_class })

    def form_valid(self, form):
        #Getting data from Form
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        #Checking credentials
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            #Invalid credentials message
            messages.add_message(self.request, messages.ERROR, 'Invalid credentials' )
            return redirect('user_auth_app:login')

class UserRegister(FormView):
    template_name = 'user_auth_app/forms/user_register_form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('user_auth_app:login')

    #Checking if user is logged
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('quests_manager:index')
        else:
            return render(request, self.template_name, { 'form' : self.form_class })

    #Getting data from Form and processing
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username = username, password = password)
        form.save()
        return super().form_valid(form)

#Loggin out user
def logout_view(request):
    logout(request)
    return redirect('home:index')
