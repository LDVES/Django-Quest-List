from django.test import TestCase, Client
from .models import Quest
# Create your views here.
class RenderQuestsListViewsTest(TestCase):

    def test_render_list_view(self):
        client = Client()
        response = client.get('/quests')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Quests")
