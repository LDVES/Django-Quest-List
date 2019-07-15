from django.test import TestCase, Client

class RenderHomepageViewsTest(TestCase):
    def test_render_index_view(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is the homepage')
# Create your tests here.
