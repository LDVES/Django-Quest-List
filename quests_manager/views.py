from django.shortcuts import render
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
        quest = Quest.objects.get(id=quest_id)
        return render(request, self.template_name, { 'quest' : quest })
