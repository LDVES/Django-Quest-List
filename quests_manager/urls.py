from django.urls import path
from quests_manager.views import ListView, DetailView, DeleteQuestView
#Namespace for quests manager
app_name='quests_manager'
urlpatterns = [
	path('', ListView.as_view(), name='index'),
	path('<int:quest_id>', DetailView.as_view(), name='detail'),
	path('<int:quest_id>/delete', DeleteQuestView.as_view(), name='delete')
]
