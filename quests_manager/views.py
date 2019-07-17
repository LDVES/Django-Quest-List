from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from .models import Quest

class ListView(View):
    template_name = 'quests_manager/index.html'
    quests = Quest.objects.all()[:5]
    def get(self, request):
        return render(request, self.template_name, { 'quests' : self.quests })

class DetailView(View):
    template_name = 'quests_manager/detail.html'
    def get(self, request, quest_id):
        quest = get_object_or_404(Quest, id=quest_id)
        return render(request, self.template_name, { 'quest' : quest })

#Deleting Quest
class DeleteQuestView(View):
    def get(self, request, quest_id):
        quest = get_object_or_404(Quest, id=quest_id)
        quest.delete()
        return HttpResponseRedirect(reverse('quests_manager:index'))
