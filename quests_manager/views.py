#View stuff
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy, reverse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages

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
from .middleware.QuestsCRUDMiddleware import (
QuestsCRUDMiddleware,
check_if_user_is_authenticated
)
#----------------------

#Quest CRUD

class QuestsList(check_if_user_is_authenticated, ListView):
    model = Quest
    context_object_name = 'quests'
    template_name = 'quests_manager/index.html'
    #Custom Middleware
    crud_middleware = QuestsCRUDMiddleware

class QuestDetail(check_if_user_is_authenticated, DetailView):
    model = Quest
    template_name = 'quests_manager/detail.html'
    #Custom Middleware
    crud_middleware = QuestsCRUDMiddleware

class QuestCreate(check_if_user_is_authenticated, CreateView, FormView):
    model = Quest
    fields = ['title', 'body']
    template_name = 'quests_manager/forms/quest_create_form.html'
    success_message = "Quest was created successfully"
    success_url = reverse_lazy("quests_manager:index")
    #Custom Middleware
    crud_middleware = QuestsCRUDMiddleware

    def form_valid(self, form):
        return self.crud_middleware.create_quest(self, form)

class QuestDelete(check_if_user_is_authenticated, DeleteView):
    model = Quest
    template_name = 'quests_manager/delete.html'
    success_url = reverse_lazy("quests_manager:index")
    success_message = "Quest was deleted successfully"
    redirect_url = 'quests_manager:index'
    #Custom Middleware
    crud_middleware = QuestsCRUDMiddleware

    def get_object(self, queryset=None):
        quest_to_delete = super(QuestDelete, self).get_object()
        return self.crud_middleware.delete_quest(self, quest_to_delete)

class QuestUpdate(check_if_user_is_authenticated, UpdateView):
    model = Quest
    form_class = QuestCreateForm
    template_name = "quests_manager/forms/quest_update_form.html"
    success_message = "Quest was updated successfully"
    #Custom Middleware
    crud_middleware = QuestsCRUDMiddleware
