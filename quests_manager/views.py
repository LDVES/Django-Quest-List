#View stuff
from django.urls import reverse_lazy, reverse
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
    form_class = QuestCreateForm
    template_name = 'quests_manager/forms/quest_create_form.html'
    success_url = reverse_lazy("quests_manager:index")

class QuestDelete(DeleteView):
    model = Quest
    template_name = 'quests_manager/delete.html'
    success_url = reverse_lazy("quests_manager:index")

class QuestUpdate(UpdateView):
    model = Quest
    form_class = QuestCreateForm
    template_name = "quests_manager/forms/quest_update_form.html"
