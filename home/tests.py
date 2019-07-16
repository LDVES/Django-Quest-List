from django.test import TestCase, Client


class RenderHomepageViewsTest(TestCase):

    #Trying to render index view
    def test_render_index_view(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is the homepage')


    #Trying to render about view
    def test_render_about_us_view(self):
        client = Client()
        response = client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About us')


    #Trying to render contact view
    def test_render_contact_view(self):
        client = Client()
        response = client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contact')
