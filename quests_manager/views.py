#View stuff
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
#DB stuff
from .models import Quest
from .forms import AddQuestForm

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

#Adding new Quest
class AddQuestView(View):
    #rendering the form
    def get(self, request):
        form =  AddQuestForm()
        return render(request, 'quests_manager/forms/AddQuestForm.html', { 'form' : form })
    #Getting and processing data from form
    def post(self, request):
        form = AddQuestForm(request.POST)
        if form.is_valid():

            quest = Quest(title = form.data['quest_title'], body = form.data['quest_body'])
            quest.title = ('title')
            quest.body = ('body')
            quest.save()

            return HttpResponseRedirect(reverse('quests_manager:index'))
