from django.test import TestCase, Client
from .models import Quest
from quests_manager.forms import AddQuestForm

class RenderListViewTest(TestCase):
    #creates Quest object
    def create_Quest_object(self):
        test_quest = Quest(title="Quest2", body="Quest2 body")
        test_quest.save()
        return test_quest

    #Testing displaying list of quests
    def test_render_list_view(self):
        quest = self.create_Quest_object()
        client = Client()
        response = client.get('/quests/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, quest.title)


    #Testing displaying empty list
    def test_render_list_view_without_any_quests(self):
        client = Client()
        response = client.get('/quests/')
        self.assertEqual(response.status_code, 200)


class RenderDetailViewTest(TestCase):
    #creates Quest object
    def create_Quest_object(self):
        test_quest = Quest(title="Quest2", body="Quest2 body")
        test_quest.save()
        return test_quest

    #Testing displaying details view
    def test_render_details_view(self):
        quest = self.create_Quest_object()
        client = Client()
        response = client.get('/quests/'+str(quest.id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, quest.title)
        self.assertContains(response, quest.body)

    #Testing displaying details view with test_render_details_view_with_incorrect_id
    def test_render_details_view_with_incorrect_id(self):
        client = Client()
        response = client.get('/quests/999')
        self.assertEqual(response.status_code, 404)

class RenderDeleteViewTest(TestCase):

    #Testing deleting Quest object
    def test_deleting_quest(self):
        quest = Quest(title="Quest3443433", body="Quest34434")
        quest.save()
        client = Client()
        quest_title = quest.title
        quest_id = quest.id
        response = client.get('/quests/'+str(quest.id)+'/delete')
        list_view_after_deletion = client.get('/quests/')
        detail_view_after_deletion = client.get('/quests/'+str(quest_id))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(detail_view_after_deletion.status_code, 404)
        self.assertNotContains(list_view_after_deletion, quest_title)

    #Testing deleting Quest object, which doesn't exist
    def test_deleting_quest_with_bad_id(self):
        client = Client()
        response = client.get('/quests/'+'error'+'/delete')
        self.assertEqual(response.status_code, 404)

class RenderQuestAddViewTest(TestCase):
    #Testing rendering QuestAdd form
    def test_rendering_form(self):
        client = Client()
        response = client.get('/quests/add')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'title')
        self.assertContains(response, 'body')
        self.assertContains(response, '</form>')

    #Testing rendering QuestAdd blank form
    def test_blank_form(self):
        client = Client()
        response = client.get('/quests/add')
        form = AddQuestForm()
        form.quest_title=''
        form.quest_body=''
        self.assertFalse(form.is_valid())
