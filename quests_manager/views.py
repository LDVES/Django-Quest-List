from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from .models import Quest

class ListView(View):
    template_name = 'quests_manager/index.html'

    def get(self, request):
        #Getting updated quests
        quests = Quest.objects.all()

        return render(request, self.template_name, { 'quests' : quests })

class DetailView(View):
    template_name = 'quests_manager/detail.html'
    def get(self, request, quest_id):
        #Getting updated quests
        quests = Quest.objects.all()

        quest = get_object_or_404(Quest, id=quest_id)
        return render(request, self.template_name, { 'quest' : quest })

#Deleting Quest
class DeleteQuestView(View):
    def get(self, request, quest_id):
        #Getting updated quests
        quests = Quest.objects.all()

        quest = get_object_or_404(Quest, id=quest_id)
        quest.delete()
        return HttpResponseRedirect(reverse('quests_manager:index'))
