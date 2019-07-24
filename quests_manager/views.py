#View stuff
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
)

#DB stuff
from .models import Quest

#Checking if user is authenticated
class CheckIfUserIsAuthenticated(LoginRequiredMixin, View):
    login_url='home:index'

#Quest CRUD

class QuestsList(CheckIfUserIsAuthenticated, ListView):
    model = Quest
    context_object_name = 'quests'
    template_name = 'quests_manager/index.html'

class QuestDetail(CheckIfUserIsAuthenticated, DetailView):
    model = Quest
    template_name = 'quests_manager/detail.html'

class QuestCreate(CheckIfUserIsAuthenticated, CreateView):
    model = Quest
    fields = ['title', 'body', 'author']
    template_name = 'quests_manager/forms/quest_create_form.html'

class QuestDelete(CheckIfUserIsAuthenticated, DeleteView):
    model = Quest
    template_name = 'quests_manager/delete.html'
    success_url = reverse_lazy("quests_manager:index")

class QuestUpdate(CheckIfUserIsAuthenticated, UpdateView):
    model = Quest
    fields = ['title', 'body']
    template_name = "quests_manager/forms/quest_update_form.html"
