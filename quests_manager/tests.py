from django.test import TestCase, Client
from .models import Quest
# Create your views here.
class RenderQuestsListViewsTest(TestCase):

    #Testing displaying list of quests
    def test_render_list_view(self):
        q1 = Quest(title="Quest2", body="Quest2 body")
        q1.save()
        client = Client()
        response = client.get('/quests')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, q1.title)
