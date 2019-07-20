from django.urls import path
from quests_manager.views import (
QuestsList,
QuestDetail,
QuestDelete,
QuestCreate,
QuestUpdate
)
#Namespace for quests manager
app_name='quests_manager'
urlpatterns = [
	path('', QuestsList.as_view(), name='index'),
	path('<int:pk>', QuestDetail.as_view(), name='detail'),
	path('<int:pk>/delete', QuestDelete.as_view(), name='delete'),
	path('add', QuestCreate.as_view(), name='add'),
	path('<int:pk>/update', QuestUpdate.as_view(), name='update'),
]
