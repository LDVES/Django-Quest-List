#View stuff
from django.urls import reverse_lazy
from django.views.generic import (
ListView,
CreateView,
DetailView,
DeleteView,
UpdateView,
)

#DB stuff
from .models import Quest

#Quest CRUD


class QuestsList(ListView):
    model = Quest
    context_object_name = 'quests'
    template_name = 'quests_manager/index.html'

class QuestDetail(DetailView):
    model = Quest
    template_name = 'quests_manager/detail.html'

class QuestCreate(CreateView):
    model = Quest
    fields = ['title', 'body']
    template_name = 'quests_manager/forms/quest_create_form.html'

class QuestDelete(DeleteView):
    model = Quest
    template_name = 'quests_manager/delete.html'
    success_url = reverse_lazy("quests_manager:index")

class QuestUpdate(UpdateView):
    model = Quest
    fields = ['title', 'body']
    template_name = "quests_manager/forms/quest_update_form.html"
