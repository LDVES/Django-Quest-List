from django.urls import path
from quests_manager.views import ListView, DetailView
#Namespace for quests manager
app_name='quests_manager'
urlpatterns = [
	path('', ListView.as_view(template_name='quests_manager/index.html'), name='index'),
	path('/<int:quest_id>', DetailView.as_view(template_name='quests_manager/detail.html'), name='detail')
]
