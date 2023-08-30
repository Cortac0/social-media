from django.test import TestCase, Client

from .models import Content

class ContentTestCase1(TestCase):
    def tes_create_post(self):
        c = Client()
        res = c.post("/create", {
            "title": "Test title",
            "text": "Some content",
        })

        assert res.status_code == 302

        posts = Content.objects.all()

        assert len(posts) == 1