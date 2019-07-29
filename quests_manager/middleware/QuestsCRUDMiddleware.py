from django.shortcuts import render, redirect
from django.http import Http404
from quests_manager.models import Quest
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

#Checking if user is authenticated
class check_if_user_is_authenticated(LoginRequiredMixin, View):
    login_url='user_auth_app:login'

class QuestsCRUDMiddleware():

    def create_quest(self, form):
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            author = self.request.user
            new_quest = Quest(title = title, body = body, author=author)
            new_quest.save()
            messages.add_message(self.request, messages.SUCCESS, self.success_message)
            return redirect(self.success_url)

    def process_quest_object(self, quest_object):
        if not quest_object.author == self.request.user:
            raise Http404
        return quest_object
