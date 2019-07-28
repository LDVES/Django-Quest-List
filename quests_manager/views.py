#View stuff
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import (
ListView,
CreateView,
DetailView,
DeleteView,
UpdateView,
FormView,
)
from .forms import QuestCreateForm
#DB stuff
from .models import Quest
#-----------------------
#Custom Middleware
from .middleware.QuestsCRUDMiddleware import QuestsCRUDMiddleware
#----------------------

#Checking if user is authenticated
class CheckIfUserIsAuthenticated(LoginRequiredMixin, View):
    login_url='user_auth_app:login'

#Quest CRUD

class QuestsList(CheckIfUserIsAuthenticated, ListView):
    model = Quest
    context_object_name = 'quests'
    template_name = 'quests_manager/index.html'

class QuestDetail(CheckIfUserIsAuthenticated, DetailView):
    model = Quest
    template_name = 'quests_manager/detail.html'

class QuestCreate(CheckIfUserIsAuthenticated, CreateView, FormView):
    model = Quest
    fields = ['title', 'body']
    template_name = 'quests_manager/forms/quest_create_form.html'
    success_message = "Quest was created successfully"
    success_url = reverse_lazy("quests_manager:index")
    #Custom Middleware
    crud_middleware = QuestsCRUDMiddleware

    def form_valid(self, form):
        return self.crud_middleware.create_quest(self, form)

class QuestDelete(CheckIfUserIsAuthenticated, DeleteView):
    model = Quest
    template_name = 'quests_manager/delete.html'
    success_url = reverse_lazy("quests_manager:index")
    success_message = "Quest was deleted successfully"

class QuestUpdate(CheckIfUserIsAuthenticated, UpdateView):
    model = Quest
    form_class = QuestCreateForm
    template_name = "quests_manager/forms/quest_update_form.html"
    success_message = "Quest was updated successfully"
