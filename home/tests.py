from django.test import TestCase, Client
from .models import Page

class RenderHomepageViewsTest(TestCase):

    #Trying to render index view
    def test_render_index_view(self):

        index_page_title = "Index page title"
        index_page_body = "Index page body"
        page = "Homepage"
        index_page = Page(title = index_page_title, body = index_page_body, page_name = page)
        index_page.save()

        client = Client()
        response = client.get('')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, index_page_title)
        self.assertContains(response, index_page_body)


    #Trying to render about view
    def test_render_about_us_view(self):

        about_page_title = "About us page title"
        about_page_body = "About us page body"
        page = "About_us"
        about_page = Page(title = about_page_title, body = about_page_body, page_name = page)
        about_page.save()

        client = Client()
        response = client.get('/about')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, about_page_title)
        self.assertContains(response, about_page_body)


    #Trying to render contact view
    def test_render_contact_view(self):

        contact_page_title = "About us page title"
        contact_page_body = "About us page body"
        page = "Contact"
        contact_page = Page(title = contact_page_title, body = contact_page_body, page_name = page)
        contact_page.save()

        client = Client()
        response = client.get('/contact')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, contact_page_title)
        self.assertContains(response, contact_page_body)
