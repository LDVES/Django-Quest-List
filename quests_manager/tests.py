from django.test import TestCase, Client
from .models import Quest
# Create your views here.
#CRUD - Create Read Update Delete
class RenderQuestsCRUDViewsTest(TestCase):
    #creates Quest object
    def create_Quest_object(self):
        test_quest = Quest(title="Quest2", body="Quest2 body")
        test_quest.save()
        return test_quest

    #Testing displaying list of quests
    def test_render_list_view(self):
        quest = self.create_Quest_object()
        client = Client()
        response = client.get('/quests')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, quest.title)

    def test_render_details_view(self):
        quest = self.create_Quest_object()
        client = Client()
        response = client.get('/quests/'+str(quest.id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, quest.title)
        self.assertContains(response, quest.body)
