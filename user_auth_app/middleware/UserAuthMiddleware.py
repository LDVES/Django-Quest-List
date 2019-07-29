from django.shortcuts import render,  redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

class UserAuthMiddleware():

    #Redirects user to redirect_url when user is authenticated
    def redirect_user_if_authenticated(self, request):
       if request.user.is_authenticated:
           return redirect(self.redirect_url)
       else:
           return render(request, self.template_name, { 'form' : self.form_class })


    #Getting data from form and logging user
    def login_user(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        #Checking credentials
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            #Invalid credentials message
            messages.add_message(self.request, messages.ERROR, 'Invalid credentials')
            return redirect('user_auth_app:login')


    #Registering user
    def register_user(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username = username, password = password)
        form.save()
        return redirect(self.success_url)
